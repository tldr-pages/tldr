# pw-cat

> Speel en neem audio-bestanden op via PipeWrite.
> Meer informatie: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- Speel een WAV bestand over de standaard target:

`pw-cat --playback {{pad/naar/bestand.wav}}`

- Speel een WAV bestand met een specifieke resampler kwaliteit (standaard 4):

`pw-cat --quality {{0..15}} --playback {{pad/naar/bestand.wav}}`

- Neem een sample recording op met een volume level van 125%:

`pw-cat --record --volume {{1.25}} {{pad/naar/bestand.wav}}`

- Neem een sample recording op met een andere sample rate:

`pw-cat --record --rate {{6000}} {{pad/naar/bestand.wav}}`

- Toon de help:

`pw-cat {{[-h|--help]}}`
