# rbash

> Cochilie restricționată Bash, echivalentă cu `bash —restricționat”.
> Nu permite modificarea directorului de lucru, redirecționarea ieșirii comenzii sau modificarea variabilelor de mediu, printre altele.
> A se vedea, de asemenea, `histexpand` pentru extinderea istoriei.
> Mai multe informaţii: <https://www.gnu.org/software/bash/manual/html_node/The-Restricted-Shell>

- Începeți o sesiune de shell interactivă:

`rbash`

- Executați o comandă și apoi ieșiți:

`rbash -c "{{command}}"`

- Execută un script:

`rbash {{path/to/script.sh}}`

- Executați un script, tipăriți fiecare comandă înainte de a o executa:

`rbash -x {{path/to/script.sh}}`

- Executați comenzi dintr-un script, oprind la prima eroare:

`rbash -e {{path/to/script.sh}}`

- Citiți și executați comenzi de la stdin:

`rbash -s`
