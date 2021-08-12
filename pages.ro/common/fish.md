# fish

> The Friendly Interactive Shell, un interpret de linie de comandă conceput pentru a fi ușor de utilizat.
> Mai multe informaţii: <https://fishshell.com>

- Începeți o sesiune de shell interactivă:

`fish`

- Executați o comandă și apoi ieșiți:

`fish -c "{{command}}"`

- Execută un script:

`fish {{path/to/script.fish}}`

- Verificați un script pentru erori de sintaxă:

`fish --no-execute {{path/to/script.fish}}`

- Începeți o sesiune de shell interactivă în modul privat, în cazul în care shell-ul nu accesează istoricul vechi sau salvează un nou istoric:

`fish --private`

- Afișează informații despre versiune și ieșire:

`fish --version`

- Setarea și exportul variabilelor de mediu care persistă în coajă repornește (numai din interiorul carcasei):

`set -Ux {{variable_name}} {{variable_value}}`
