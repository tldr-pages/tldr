# vcsh

> Sistem de control al versiunii pentru directorul de acasă utilizând depozitele Git.
> Mai multe informaţii: <https://github.com/RichiH/vcsh>

- Inițializarea unui depozit (gol):

`vcsh init {{repository_name}}`

- Clonează un depozit într-un nume de director personalizat:

`vcsh clone {{git_url}} {{repository_name}}`

- Lista tuturor depozitelor gestionate:

`vcsh list`

- Executați o comandă Git pe un depozit gestionat:

`vcsh {{repository_name}} {{git_command}}`

- Împingeți/trageți toate depozitele gestionate la/de la telecomenzi:

`vcsh {{push|pull}}`

- Scrieți un fișier personalizat `.gitignore` pentru un depozit gestionat:

`vcsh write-gitignore {{repository_name}}`
