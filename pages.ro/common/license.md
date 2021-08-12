# license

> Creați fișiere de licență pentru proiecte open-source.
> Mai multe informaţii: <https://nishanths.github.io/license>

- Imprimați o licență pentru stdout, utilizând valorile implicite (numele autorului detectat automat și anul curent):

`license {{license_name}}`

- Generați o licență și salvați-o într-un fișier:

`license -o {{filename}} {{license_name}}`

- Listează toate licențele disponibile:

`license ls`

- Generați o licență cu numele de autor personalizat și anul:

`license --name {{author}} --year {{release_year}} {{license_name}}`
