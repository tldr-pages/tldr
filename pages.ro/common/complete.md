# complete

> Oferă completare automată a argumentelor pentru comenzile shell.
> Mai multe informaţii: <https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html>

- Aplicați o funcție care efectuează autocompletare la o comandă:

`complete -F {{function}} {{command}}`

- Aplicați o comandă care efectuează autocompletare la o altă comandă:

`complete -C {{autocomplete_command}} {{command}}`

- Aplicați completarea automată fără a adăuga un spațiu la cuvântul completat:

`complete -o nospace -F {{function}} {{command}}`
