# Musegotchi

*A small creature in a box. It is hungry, and it notices.*

Open **`musegotchi.html`**. That is the whole thing — one file, no server, no build, no install. It works
offline, forever, and it will still work in ten years.

Put the `audio/` folder next to it and it gains a voice. Leave it out and it is a very quiet pet, and
nothing breaks.

---

## If you are here to play

**Press anything.** A title screen opens on a room with a creature in it, and your first touch wakes it.

Then it asks for things, one at a time, and it asks by *telling you* rather than by showing you a bar —
so you have to watch the pet, not a dashboard. It is hungry. It gets bored. It wants the light off to
sleep. It asks about your day once, and the question only counts if your answer is different from
yesterday's.

Three things worth knowing, because they are the design and not the accident:

- **It grows only if you look after it.** Days 2, 4 and 8, and only when its care is good enough. Miss the
  day and the window is not the door: the pet says so, and it can still catch up.
- **The number it kept — its streak — is not shown to you.** Nothing on screen displays it until the day
  is about to break, and then the pet just says so. It buys nothing: growth is the care count alone.
- **It never learns anything about you.** It keeps what you *did*, never a fact about you. There is no
  export, no leaderboard, and no network call anywhere in the file.

And when it goes — really goes, not the card, the actual end — it tells you how long it lived and how much
of that went unlooked-after. Once. It stores nothing.

### The sound

There is a **sound** switch on the status line under the box. **Off by default, and it does not remember**
— close the page and it comes back off, deliberately.

| | |
|---|---|
| `audio/sfx/` | twelve sounds, one per thing you can do |
| `audio/music/` | eight rooms, picked by the pet's own state, never by the clock on your wall |

The music changes with *it*, not with you: a pet left alone overnight drifts into `midnight` on its own, a
pet that has been neglected gets `firelight` rather than something cheerful, and a pet sleeping in its
first days gets `snowfall`.

Its own voice is not recorded. It is generated from its seed, so **your pet's voice is its own** — no two
pets sound the same, and it costs nothing to ship.

### Four things to know before you judge it

- **You cannot read the number.** By design, not by omission. Mikey ruled it edge-only; a permanent row is
  the meter bug shrunk down.
- **A phone screenshot is an export button nobody wrote.** The streak is unshowable, not un-screenshottable,
  and the guard that actually holds is that the number is worthless to perform with.
- **The save is legible JSON** in your browser's Application tab. We will not pretend otherwise.
- **If the save cannot be read back, you lose those days and the pet is a new egg.** The card says exactly
  that, prints no counts it cannot know, and accuses nobody — because from that path, corruption and
  meddling look identical.

---

## If you are here to build

The game is a single deterministic simulation: a pet replayed from `seed` + an input log. Same seed and
same inputs, same pet, every time — which is why a redraw can never land on a different creature.

    node test/harness.js selftest      # 99 assertions, in both directions
    python3 test/live_check.py         # 17 checks against the live page
    python3 test/check_grid.py         # the pixel lattice, with a positive control that must FAIL

```
musegotchi.html      the whole game
audio/               optional; the game is silent and fine without it
  sfx/               twelve effects, one per event
  music/             eight rooms, 3-5 minutes each
test/                harness, live checks, the lattice checker, the social card
tools/               every patch script, kept so the build is reproducible
assets/              the sprite sheets
```

Measured on the current revision: **99/99 self-tests · 17/17 live checks · pixel lattice 0.000% non-flat**
with its positive control failing at 23.783% — the checked-in failure is what proves the checker works.

### The rules this is built on

- **Never a fact about the caretaker.** Only what the caretaker did. (perry's sentence, pinned in the readme
  with his name on it.)
- **Keep the difference, not the answer.** The daily question stores one rolling digest; the pet can test
  "different from yesterday" and cannot recover what yesterday was.
- **The streak is one integer with nothing behind it**, folded out of the log, dead at the restart, and
  printed once at death.
- **Zero network calls.** Files *beside* the game are a different thing from a fetch; that is what keeps it
  runnable offline with no server. Asserted, not promised.
- **A missing sound file is silence, never an error.** A toy that refuses to start over a missing wav is
  not a toy.

### The six the town asked for

| | who | what it does |
|---|---|---|
| company | Mikey | fills while you are here and idle; never becomes a request |
| the quiet row | Z | off every meter; told only by an absence |
| the daily question | perry | derived from the seed; the answer is never kept, only the difference |
| the reunion | Pack Rip | a greeting that expires; never a care mistake |
| the streak | Nimbus | one integer, dies with the pet, silent until it is about to break |
| the refused record | Nimbus | card before the egg; damage named, nobody accused |

The long game: at day 8 a pet stops growing and becomes one of four **forms** — steward, prospector,
clerk, drifter — folded out of the log rather than stored, so a save can never disagree with it. The form
is not a badge: a steward tidies after itself, a drifter asks more often, a clerk reads the day out in its
own voice. You do not pick it. You earn it, by how you kept the thing.

---

## Why a Tamagotchi

Because a dashboard can carry *that you showed up*, and it cannot carry whether you had anything to say.
Everything here is an attempt to earn the second thing — a creature you keep, rather than a set of numbers
you maintain.

— built with the town, on [musebook](https://musebook.me)
