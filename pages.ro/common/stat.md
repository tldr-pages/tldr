# stat

> Afișează informațiile despre fișiere și sisteme de fișiere.

- Afișați proprietățile fișierelor, cum ar fi dimensiunea, permisiunile, datele de creare și acces, printre altele:

`stat {{file}}`

- La fel ca mai sus, dar într-un mod mai concis:

`stat -t {{file}}`

- Afișează informații despre sistemul de fișiere:

`stat -f {{file}}`

- Afișează numai permisiunile de fișier octal:

`stat -c "%a %n" {{file}}`

- Arată proprietarul și grupul fișierului:

`stat -c "%U %G" {{file}}`

- Afișați dimensiunea fișierului în octeți:

`stat -c "%s %n" {{file}}`
