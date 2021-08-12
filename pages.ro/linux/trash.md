# trash

> Un CLI pentru gestionarea coșului de gunoi /coșul de reciclare.
> Mai multe informaţii: <https://github.com/andreafrancia/trash-cli>

- Ștergeți un fișier (trimiteți la coșul de gunoi):

`trash {{path/to/file}}`

- Lista fișierelor în coșul de gunoi:

`trash-list`

- Restaurați fișierul din coșul de gunoi:

`trash-restore`

- Goliţi gunoiul:

`trash-empty`

- Goliți coșul de gunoi, păstrând fișierele distruse cu mai puțin de {10}} zile în urmă:

`trash-empty {{10}}`

- Eliminați toate fișierele denumite „foo” din coșul de gunoi:

`trash-rm foo`

- Eliminați toate fișierele cu o locație originală dată:

`trash-rm {{/absolute/path/to/file_or_directory}}`
