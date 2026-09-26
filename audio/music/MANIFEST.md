# Musegotchi — audio

Generated with the operator's ElevenLabs key on 2026-09-25. **This folder is optional: the game runs
perfectly without it.** A missing file is silence, never an error.

    audio/
      sfx/      twelve effects, one per game event, dry and toy-sized
      music/    three lo-fi rooms, 60s each, looped

## The rules the audio lives by

- **No network.** The game makes zero fetch/XHR calls. Files *beside* it are a different thing from a
  fetch — that is what keeps it runnable offline, forever, with no server.
- **Not inlined, on purpose.** The four spoken moments were inlined at 22kHz/32k and cost 76KB of
  base64; inlining the music would have made the file ~20x its size. The operator's ruling was that
  depth is worth more than a 404KB artefact, so audio became a sidecar and the game got *smaller*.
- **Off by default, and not persisted.** The save holds exactly one localStorage key (rules P4/P6), so
  the sound and music switches live in memory for the session. Close the page and they return to off.
- **Music follows the pet's clock, not the caretaker's** — a pet left alone overnight goes to `midnight`
  on its own. Three rooms: `daylight`, `evening` (lights off, or day 2+), `midnight` (asleep).
- **No vocals, ever.** A lo-fi bed under a sleeping creature is the whole idea; a voice would be a
  performance and this is a room.

## Regenerating

    make_sfx.py     # 12 effects, ~1s each
    make_music.py   # 3 tracks, 60s each (music is billed per SECOND, not per character)
    probe_music.py  # one 45s track, to measure the unit price before spending

Music spend so far: 180 seconds (45s probe + 3x60s). Voice spend: ~6.7k characters.
