# bison

> Generator de parser GNU.
> Mai multe informaţii: <https://www.gnu.org/software/bison/>

- Compilarea unui fișier de definiție bizon:

`bison {{path/to/file.y}}`

- Compilați în modul de depanare, ceea ce determină parserul rezultat să scrie informații suplimentare la ieșirea standard:

`bison --debug {{path/to/file.y}}`

- Specificați numele fișierului de ieșire:

`bison --output {{path/to/output.c}} {{path/to/file.y}}`

- Fiți verbose atunci când compilați:

`bison --verbose`
