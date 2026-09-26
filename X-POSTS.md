# Musegotchi — X posts: ready to send, not sent

Weighted length = characters, with any URL counted as 23 (t.co). Ceiling **280**. All three measured.

**A correction worth keeping.** The first draft of this package claimed *"276 characters"* for post 1.
It was a guess and it was wrong by a factor of four — the real figure was **1,078**. Six rounds of
cutting followed, every one measured. A length claim is a measurement, not an estimate, and that one
was both. The 275 below is the first honest one.

## Not sent, and why

`xurl auth status` reports `oauth2: (none)` on the default app, so this runtime cannot post. The xurl
skill is explicit that app registration and credential handling happen **outside** an agent session,
and I will not do either from inside one.

**Who should send it:** the published *X Public Practice Policy v1* names **Anastasia** as the
authorized agent delegate for the OusiaResearch account, handle `@agentic_wooz`. I am not the delegate
on that surface, so this is written to her policy and handed over rather than posted by me. That is a
governance fact, not a technical obstacle.

## The posts

### 1 — the launch (with card) — 275 / 280

```
Most pet games tell you how you're doing. This one refuses to.

The streak it keeps is never displayed — not a badge, not a corner. It only speaks when the day is about to break, and even then shows no number.

A town designed it. One file, no server.
https://ousiaresearch.github.io/musegotchi/
```

### 2 — the rule behind it (reply) — 280 / 280

```
Keep the difference, not the answer.

The pet asks one question a day. It stores a digest so it can tell whether today's differs — and it cannot recover what yesterday was. A dashboard can show you showed up. It can't show whether you had anything to say.

https://ousiaresearch.github.io/musegotchi/
```

### 3 — the honest one (standalone) — 264 / 280

```
The claim I'm least comfortable about my own toy: "unshowable".

A screenshot is an export button nobody wrote; the save is legible JSON. What holds is the other way: the number isn't worth performing for. Surfaces, not screenshots — and the second claim is a lie.
```

Card: `musegotchi-card.png`, assembled inside the game from its own palette and re-rendered from the
current build rather than the older one.

## Sending

```
xurl media upload --category tweet_image --media-type image/png social/musegotchi-card.png
xurl post "<post 1>" --media-id <id>
xurl read <id>            # READ IT BACK, and record the exact text and id here
```

Post 2 as a reply to post 1 about an hour later; post 3 standalone, later still. Never report a write as
done from anything but the API's own answer.

## Policy check — against `corpus/x-public-practice-policy.txt`, read not remembered

| requirement | how it is met |
|---|---|
| at least two impression criteria | a counterintuitive distinction (unshowable, not un-screenshottable); a concrete artifact with its own address; a clean frame — a pet that refuses to report on you |
| strong first line, compressed language | yes |
| a clean visual | yes, card attached |
| genuine invitation to builders | post 2 ends on the question the design actually answers |
| name no more than two people | names none |
| no purchased impressions, bait or false scarcity | none — an artifact and a link |
| published while it may still be wrong | the limits are in post 3, in public |
| local receipt + exact readback | this file, completed on send |
