# jest

> O platformă de testare JavaScript cu configurație zero.
> Mai multe informaţii: <https://jestjs.io>

- Rulați toate testele disponibile:

`jest`

- Rulați suitele de testare din fișierele date:

`jest {{path/to/file1}} {{path/to/file2}}`

- Rulați suitele de testare din fișierele din actualele și subdirectoarele, ale căror căi se potrivesc cu expresia regulată dată:

`jest {{regular_expression1}} {{regular_expression2}}`

- Rulați testele ale căror nume se potrivesc cu expresia regulată dată:

`jest --testNamePattern {{regular_expression}}`

- Rulați suitele de testare legate de un fișier sursă dat:

`jest --findRelatedTests {{path/to/source_file.js}}`

- Rulați suitele de testare legate de toate fișierele neangajate:

`jest --onlyChanged`

- Uita-te la fisiere pentru modificari si re-rula automat teste legate:

`jest --watch`

- Arată ajutor:

`jest --help`
