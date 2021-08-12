# bash

> Bourne-Again Shell, un interpret de linie de comandă `sh`-compatibil.
> A se vedea, de asemenea, `histexpand` pentru extinderea istoriei.
> Mai multe informaţii: <https://gnu.org/software/bash/>

- Începeți o sesiune de shell interactivă:

`bash`

- Executați o comandă și apoi ieșiți:

`bash -c "{{command}}"`

- Execută un script:

`bash {{path/to/script.sh}}`

- Executați un script, tipăriți fiecare comandă înainte de a o executa:

`bash -x {{path/to/script.sh}}`

- Executați comenzi dintr-un script, oprind la prima eroare:

`bash -e {{path/to/script.sh}}`

- Citiți și executați comenzi de la stdin:

`bash -s`

- Imprimați versiunea Bash (`$BASH_VERSION' conține versiunea fără informații despre licență):

`bash --version`
