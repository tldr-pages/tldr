# readelf

> Afișează informații despre fișierele ELF.
> Mai multe informaţii: <http://man7.org/linux/man-pages/man1/readelf.1.html>

- Afișează toate informațiile despre fișierul ELF:

`readelf -all {{path/to/binary}}`

- Afișează toate anteturile prezente în fișierul ELF:

`readelf --headers {{path/to/binary}}`

- Afișează intrările în secțiunea tabelului simbol a fișierului ELF, dacă are unul:

`readelf --symbols {{path/to/binary}}`

- Afișați informațiile conținute în antetul ELF la începutul fișierului:

`readelf --file-header {{path/to/binary}}`
