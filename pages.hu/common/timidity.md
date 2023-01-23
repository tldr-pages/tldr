# timidity

> A TiMidity++ egy MIDI fájllejátszó és -konvertáló. További információ: <http://timidity.sourceforge.net>.

- MIDI fájl lejátszása:

`timidity {{path/to/file.mid}}`

- Egy MIDI fájl lejátszása ciklusban:

`timidity --loop {{path/to/file.mid}}`

- MIDI-fájl lejátszása egy adott hangnemben (0 = C-dúr/A-moll, -1 = F-dúr/D-moll, +1 = G-dúr/E-moll stb.):

`timidity --force-keysig={{-flats|+sharps}} {{path/to/file.mid}}`

- MIDI-fájl átalakítása PCM (WAV) audióvá:

`timidity --output-mode={{w}} --output-file={{path/to/file.wav}} {{path/to/file.mid}}`

- MIDI-fájl átalakítása FLAC audióvá:

`timidity --output-mode={{F}} --output-file={{path/to/file.flac}} {{path/to/file.mid}}`
