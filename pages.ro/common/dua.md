# dua

> Dua (Disk Usage Analyzer) este un instrument pentru a afla în mod convenabil despre utilizarea spațiului pe disc al unui anumit director.
> Mai multe informaţii: <https://github.com/Byron/dua-cli>

- Analizează directorul specific:

`dua {{path/to/directory}}`

- Afișează dimensiunea aparentă în loc de utilizare a discului:

`dua --apparent-size`

- Numără fișierele hard-legate de fiecare dată când sunt văzute:

`dua --count-hard-links`

- Agregați spațiul consumat al unuia sau mai multor directoare sau fișiere:

`dua aggregate`

- Lansarea interfeței cu utilizatorul terminalului:

`dua interactive`

- Formatul de imprimare a octeților:

`dua --format {{metric|binary|bytes|GB|GiB|MB|MiB}}`

- Setați numărul de fire care urmează să fie utilizate:

`dua --threads {{count}}`
