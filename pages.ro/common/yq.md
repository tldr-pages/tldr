# yq

> Un procesor YAML ușor și portabil de linie de comandă.
> Mai multe informaţii: <https://mikefarah.gitbook.io/yq/>

- Ieșiți un fișier YAML, în format destul de tipărit (v4+):

`yq eval {{path/to/file.yaml}}`

- Ieșiți un fișier YAML, în format destul de tipărit (v3):

`yq read {{path/to/file.yaml}} --colors`

- Ieșiți primul element dintr-un fișier YAML care conține doar o matrice (v4+):

`yq eval '.[0]' {{path/to/file.yaml}}`

- Ieșiți primul element dintr-un fișier YAML care conține doar o matrice (v3):

`yq read {{path/to/file.yaml}} '[0]'`

- Setați (sau suprascrieți) o cheie pentru o valoare dintr-un fișier (v4+):

`yq eval '.{{key}} = "{{value}}"' --inplace {{path/to/file.yaml}}`

- Setați (sau suprascrieți) o cheie pentru o valoare dintr-un fișier (v3):

`yq write --inplace {{path/to/file.yaml}} '{{key}}' '{{value}}'`

- Îmbinați două fișiere și imprimați la stdout (v4+):

`yq eval-all 'select(filename == "{{path/to/file1.yaml}}") * select(filename == "{{path/to/file2.yaml}}")' {{path/to/file1.yaml}} {{path/to/file2.yaml}}`

- Mergeți două fișiere și imprimați la stdout (v3):

`yq merge {{path/to/file1.yaml}} {{path/to/file2.yaml}} --colors`
