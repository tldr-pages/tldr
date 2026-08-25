# pw-cat

> Play and record audio files through PipeWire.
> See also: `wpctl`, `pw-cli`.
> More information: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- Play a WAV file over the default target:

`pw-cat {{[-p|--playback]}} {{path/to/file.wav}}`

- Play a MIDI file:

`pw-cat {{[-pm|--playback --midi]}} {{path/to/file.mid}}`

- Play a DSD file:

`pw-cat {{[-pd|--playback --dsd]}} {{path/to/file.dsf}}`

- Play a compressed audio file using passthrough (requires FFmpeg integration):

`pw-cat {{[-po|--playback --encoded]}} {{path/to/file.ac3}}`

- Play a WAV file with a specified resampler quality (4 by default):

`pw-cat {{[-p|--playback]}} {{[-q|--quality]}} {{0..15}} {{path/to/file.wav}}`

- Record a MIDI file:

`pw-cat {{[-rm|--record --midi]}} {{path/to/file.mid}}`

- Record a sample recording at a volume level of 125%:

`pw-cat {{[-r|--record]}} --volume {{1.25}} {{path/to/file.wav}}`

- Record a sample recording using a different sample rate:

`pw-cat {{[-r|--record]}} --rate {{6000}} {{path/to/file.wav}}`
