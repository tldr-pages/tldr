# flac

> Kódolja, dekódolja és teszteli a FLAC fájlokat. További információ: <https://xiph.org/flac>.

- Egy WAV-fájlt FLAC-ba kódol (ez egy FLAC-fájlt hoz létre a WAV-fájl helyével megegyező helyen):

`flac {{path/to/file.wav}}`

- WAV fájl kódolása FLAC-be, a kimeneti fájl megadásával:

`flac -o {{path/to/output.flac}} {{path/to/file.wav}}`

- FLAC fájl dekódolása WAV-ba, a kimeneti fájl megadásával:

`flac -d -o {{path/to/output.wav}} {{path/to/file.flac}}`

- FLAC fájl tesztelése a helyes kódolásra:

`flac -t {{path/to/file.flac}}`
