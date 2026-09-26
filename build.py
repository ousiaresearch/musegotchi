#!/usr/bin/env python3
"""Build the public page from the QA record and the game artifact."""
import hashlib, html, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
QA=Path.home()/".hermes/agents/isildur/record/qa-state.json"
KEYS=("SELF_TESTS","LIVE_CHECKS","LATTICE","CONTROL","GAME_BYTES","SHA256_SHORT","NETWORK_CALLS","MEASUREMENT_STATUS","PROVENANCE")
def values():
    out={k:"unavailable" for k in KEYS}; artifact=None
    try:
        raw=(ROOT/"musegotchi.html").read_bytes(); text=raw.decode(); digest=hashlib.sha256(raw).hexdigest()
        artifact={"bytes":len(raw),"digest":digest}; calls=sum(text.count(x) for x in ("fetch(","XMLHttpRequest","sendBeacon"))
        out.update(GAME_BYTES=f"{len(raw):,} bytes",SHA256_SHORT=f"{digest[:16]}…",NETWORK_CALLS=str(calls))
    except (OSError,UnicodeDecodeError): pass
    try:
        q=json.loads(QA.read_text()); required=("measured","self_tests","live_checks","lattice","control","note","game_bytes","sha256")
        if any(k not in q for k in required): raise ValueError("incomplete QA record")
        if artifact and (int(q["game_bytes"])!=artifact["bytes"] or not artifact["digest"].startswith(str(q["sha256"]))): raise ValueError("QA record does not match artifact")
        out.update(SELF_TESTS=str(q["self_tests"]),LIVE_CHECKS=str(q["live_checks"]),LATTICE=str(q["lattice"]),CONTROL=str(q["control"]),MEASUREMENT_STATUS=f"Measured {q['measured']} against this artifact.",PROVENANCE=str(q["note"]))
    except (OSError,ValueError,TypeError,json.JSONDecodeError):
        out["MEASUREMENT_STATUS"]="QA source unavailable. No cached QA figures are shown."
        out["PROVENANCE"]="Artifact figures are read directly from musegotchi.html at build time."
    return out
def main():
    page=(ROOT/"index.template.html").read_text()
    for key,value in values().items(): page=page.replace("{{"+key+"}}",html.escape(value))
    if "{{" in page: raise SystemExit("unresolved template token")
    (ROOT/"index.html").write_text(page)
    print("built index.html")
if __name__=="__main__": main()
