# Musegotchi — project page redesign

**For:** a Codex session (GPT-5.1 / "SOL"), working in `/Users/johannross/Projects/musegotchi-page`
**Status:** the page is live and correct. It is not *good*. This brief is for making it good.
**Do not break:** the contract in §6. It is the whole reason this account publishes anything.

---

## 1. What exists now, measured

| | the-formulary | musegotchi (current) |
|---|---|---|
| `index.html` | 25,488 B | 5,753 B |
| `<script>` blocks | 14 | 0 |
| inline SVG | 1 (a real diagram) | 0 |
| external CSS | 1 | 1 (borrowed from the front door) |
| runtime behaviour | interactive | **none** |

The current page is a document wearing a page's clothes. It has correct text, correct numbers, and
correct links, and it does nothing at all.

## 2. What it must become

A project page as good as the Formulary's — which means **it has to work**, not merely read. Concretely,
the pet is the subject, so the page should be *about the pet doing something* rather than about a pet.

**Non-negotiable, in priority order:**

1. **The game is the hero, above the fold.** The iframe is currently third on the page, after a heading
   and two paragraphs. Move it up. On a 1440×900 viewport a visitor should see a living creature before
   they read a word about it. The page exists to get someone to press something.
2. **Real state, read from the artifact — never retyped.** The numbers on the page (99/99, 17/17,
   0.000% non-flat, 23.783% control, 343,151 bytes, `f2121b77715d740c…`) are in `index.html` as literal
   text. They are correct today and will silently rot. See §5 — they must be injected from
   `qa-state.json` or a build step, with a visible "measured on" date.
3. **Motion with a reason.** The Formulary earns its scripts. Anything that moves here must move *because
   the pet moves*: the embedded game already has its own feedback layer (flourishes on touch, a growth
   ring, a visible ask). The page should not add decorative animation on top of that — it should get out
   of the way and let the game be the only thing moving.
4. **It must work on a phone.** The iframe is `height:1150px` fixed, which will either crop or scroll
   badly on a narrow viewport. The game is 160×144 in-world but renders responsively; the page must not
   fight it.
5. **Dark mode is already handled** via `prefers-color-scheme` in the appended CSS — keep that.

**Deliberately not wanted:**

- No parallax, no scroll-jacking, no hero video, no cursor followers, no typewriter effects.
- Nothing that animates on scroll for its own sake. The subject is a creature that only moves when you
  touch it; a page that moves on its own contradicts it.
- No third-party anything. No fonts from a CDN, no analytics, no embeds. The whole house rule is a page
  you can read in ten years.

## 3. Structure

Follow the Formulary's shape, which is: one strong opening, a short orienting line, then sections that
each demonstrate rather than describe.

```
header          Musegotchi + one line. No paragraph.
THE GAME        the live iframe, large, immediately visible
THE THREE       the design decisions that are features, not accidents
                (the streak is never shown / it learns no fact about you /
                 the window is not the door) — one card each
THE FOUR FORMS  steward · prospector · clerk · drifter, and what each DOES
THE NUMBERS     the table, injected, with the failing control shown as failing
THE SOUND       12 effects, 8 rooms; the room is chosen by the pet's state
LIMITS          the honest list, up front, not in a footer
footer          links + Content-Signal
```

**Tone:** the front door's. Precise, unhurried, willing to state a limit. No "amazing", no "cute", no
exclamation marks. The game is charming; the page that documents it should be straight.

## 4. Visual language

Already fixed, and it is a good palette — the game's own 27 world tones, measured from the sprite sheets,
with one indigo line colour (`#110452` / `#0F033C` / `#0A0238`).

- **Use the front door's `style.css` as the base** — it is already the site's type and spacing, and a
  project page that disagrees with the front door looks like a different organisation.
- **Then override toward the game's palette.** The current page is a generic documentation page wearing
  the front door's clothes. It should look like it belongs to this game.
- The card at `musegotchi-card.png` (1600×900) is the visual reference for the game's own art direction.
  Look at it before choosing type colours.
- A sprite from `assets/` used as a small decorative accent is welcome. Nothing larger than 64px.

## 5. Do not let the numbers rot

Today they are literals in `index.html`. That is the flaw most likely to survive a redesign, because the
page looks correct the whole time it is lying.

**Requirement:** every figure in §3's *THE NUMBERS* section comes from a source of truth, and the page
carries the date it was measured. Two acceptable routes:

- **Build step (preferred).** A `build.py` in this repo reads
  `~/.hermes/agents/isildur/record/qa-state.json` and the sha256 of `musegotchi.html`, substitutes them
  into a template, and writes `index.html`. This mirrors what the front door already does with
  `scripts/build.py` and `sources.yaml` — check `~/Projects/ousia-front-door/scripts/build.py` for the
  house pattern and match it.
- **Injected at load.** The page fetches the numbers and renders them, with a visible fallback if the
  fetch fails. **This breaks the house rule** (the page must be readable with no network) unless the
  literals remain as the fallback. If you take this route, the static numbers stay in the HTML and the
  fetch only *upgrades* them.

**If the source of truth is unavailable, the page must say so** — not render a stale number as if it were
current. "Measured 2026-09-26" next to a stale figure is honest; a bare stale figure is not.

## 6. The contract — what must remain true

The front door's own claim is *"a record you can check"*, and this page is part of that record. These are
not style preferences:

1. **The game must still make zero network calls.** `grep -c 'fetch(' musegotchi.html` must be 0, and so
   must `XMLHttpRequest` and `sendBeacon`. The game is published as a single file that runs offline; this
   is the property that makes it a toy rather than a website. **Do not add a CDN, a font link, or an
   analytics snippet to the page either** — the same rule applies one level up.
2. **The audio must stay optional.** The game is complete and silent without `audio/`. Never make the
   page's loading depend on a track existing.
3. **`llms.txt` and `agent.json` stay accurate.** The repo's whole convention is that a machine reader
   gets the same truth as a human. If the game changes, those two files change with it.
4. **The failing control stays visible.** The pixel-lattice checker's positive control is published
   *failing* at 23.783%, and it must stay on the page. A checker that cannot fail is not evidence, and
   hiding it would be the single most dishonest thing this page could do.
5. **Zero `data:` audio URIs.** The four inlined spoken clips were removed deliberately when the operator
   ruled that depth beats a 400KB artefact. `grep -c 'data:audio' musegotchi.html` must be 0.

## 7. Verify before you claim it works

```bash
# the game is untouched
shasum -a 256 musegotchi.html        # must be f2121b77715d740c…
grep -c 'fetch(' musegotchi.html     # must be 0
grep -c 'data:audio' musegotchi.html # must be 0

# the page still serves everything
for p in "" musegotchi.html llms.txt agent.json audio/music/kitchen.mp3 audio/sfx/feed.mp3; do
  curl -s -o /dev/null -w "%{http_code} $p\n" -L "https://ousiaresearch.github.io/musegotchi/$p"
done
```

**Then look at it.** A 200 means the bytes arrived, not that the page is good. Open it at 1440×900 and at
390×844, with sound on and off, and judge it as a visitor who has never seen the game.

## 8. Style

- Match `~/Projects/ousia-front-door/assets/style.css` conventions; the site's own code is the reference
  for how it writes HTML.
- Comments carry the *why*, not the what. The front door's code does this well.
- No new build tooling beyond what §5 asks for. No npm, no bundler, no framework. The Formulary is plain
  HTML, CSS and a handful of scripts; this page should be the same.
- If you add a script, it earns its place the way the Formulary's do: something on the page does not work
  without it.

## 9. What is already good and should survive

- The honest numbers table, including the failing control.
- The four forms, stated as what each one *does* rather than what it is called.
- The limits, stated plainly rather than buried.
- The read policy: `search=yes, ai-input=yes, ai-train=no`.
- The measured sha256, which makes the artifact checkable by anyone.

None of that needs rewriting. It needs a page worthy of it.
