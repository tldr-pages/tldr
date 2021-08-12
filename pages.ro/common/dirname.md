# dirname

> Calculează directorul părinte al unui anumit fișier sau al unei căi de director.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/dirname>

- Calculați directorul părinte al unei căi date:

`dirname {{path/to/file_or_directory}}`

- Calculați directorul părinte al mai multor căi:

`dirname {{path/to/file_a}} {{path/to/directory_b}}`

- Delimitarea ieșirii cu un caracter NUL în loc de o linie nouă (utilă atunci când se combină cu `xargs `):

`dirname --zero {{path/to/directory_a}} {{path/to/file_b}}`
