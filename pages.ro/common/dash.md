# dash

> Debian Almquist Shell, o implementare modernă, compatibilă cu POSIX a `sh` (nu este compatibilă cu BASH).
> Mai multe informaţii: <https://manned.org/dash>

- Începeți o sesiune de shell interactivă:

`dash`

- Executați o comandă și apoi ieșiți:

`dash -c "{{command}}"`

- Execută un script:

`dash {{path/to/script.sh}}`

- Rulați comenzi dintr-un script, tipăriți fiecare comandă înainte de a o executa:

`dash -x {{path/to/script.sh}}`

- Executați comenzi dintr-un script, oprind la prima eroare:

`dash -e {{path/to/script.sh}}`

- Citiți și executați comenzi de la stdin:

`dash -s`
