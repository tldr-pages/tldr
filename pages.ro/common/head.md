# head

> Ieșiți prima parte a fișierelor.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/head>

- Ieșiți primele câteva linii ale unui fișier:

`head -n {{count_of_lines}} {{filename}}`

- Ieșiți primii câțiva octeți ai unui fișier:

`head -c {{size_in_bytes}} {{filename}}`

- Ieșire totul, dar ultimele câteva linii ale unui fișier:

`head -n -{{count_of_lines}} {{filename}}`

- Ieșire totul, dar ultimii câțiva octeți ai unui fișier:

`head -c -{{size_in_bytes}} {{filename}}`
