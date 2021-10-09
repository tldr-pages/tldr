# timidity

> TiMidity++ is a MIDI file player and convertor.
> More information: <http://timidity.sourceforge.net>.

- Play a MIDI file:

`timidity {{path/to/file.mid}}`

- Play a MIDI file in a loop:

`timidity --loop {{path/to/file.mid}}`

- Play a MIDI file in a specific key (0 = C major/a minor, -1 = F major/d minor, +1 = G major/e minor etc.):

`timidity --force-keysig={{-flats|+sharps}} {{path/to/file.mid}}`

- Convert a MIDI file to PCM (WAV) audio:

`timidity --output-mode={{w}} --output-file={{path/to/file.wav}} {{path/to/file.mid}}`

- Convert a MIDI file to FLAC audio:

`timidity --output-mode={{F}} --output-file={{path/to/file.flac}} {{path/to/file.mid}}`
