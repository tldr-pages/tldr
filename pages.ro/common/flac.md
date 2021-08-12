# flac

> Codifică, decodifică și testează fișiere flac.
> Mai multe informaţii: <https://xiph.org/flac>

- Codificați un fișier wav la flac (acest lucru va crea un fișier flac în aceeași locație ca fișierul wav):

`flac {{path/to/file.wav}}`

- Codificați un fișier wav la flac, specificând fișierul de ieșire:

`flac -o {{path/to/output.flac}} {{path/to/file.wav}}`

- decodează un fișier flac la wav, specificând fișierul de ieșire:

`flac -d -o {{path/to/output.wav}} {{path/to/file.flac}}`

- Testați un fișier flac pentru codificarea corectă:

`flac -t {{path/to/file.flac}}`
