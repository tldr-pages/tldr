# kate

> Editor text KDE.
> Mai multe informaţii: <https://kate-editor.org/>

- Lansați Kate și deschideți fișiere specifice:

`kate {{path/to/file1}} {{path/to/file2}}`

- Deschideți un document la distanță în Kate:

`kate {{https://example.com/path/to/file}}`

- Lansați Kate, creând o nouă instanță, chiar dacă una este deja deschisă:

`kate --new`

- Deschideți un fișier în Kate cu cursorul la linia specifică:

`kate --line {{line_number}} {{path/to/file}}`

- Deschideți un fișier în Kate cu cursorul la linia și coloana specifică:

`kate --line {{line_number}} --column {{column_number}} {{path/to/file}}`

- Lansați Kate, creând un nou fișier temporar cu conținut citit din stdin:

`cat {{path/to/file}} | kate --stdin`

- Ajutor pentru afișare:

`kate --help`
