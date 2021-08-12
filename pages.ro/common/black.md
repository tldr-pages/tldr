# black

> Un formator de cod auto Python.
> Mai multe informaţii: <https://github.com/psf/black>

- Formatarea automată a unui fișier sau a unui director întreg:

`black {{path/to/file_or_directory}}`

- Formatați codul trecut ca șir:

`black -c {{path/to/file_or_directory}}`

- Ieșiți un dif pentru fiecare fișier pe stdout:

`black --diff {{path/to/file_or_directory}}`

- Returnați starea fără a scrie fișierele înapoi:

`black --check {{path/to/file_or_directory}}`

- Auto-formatați un fișier sau director care emite mesaje de eroare exclusiv la stderr:

`black --quiet {{path/to/file_or_directory}}`
