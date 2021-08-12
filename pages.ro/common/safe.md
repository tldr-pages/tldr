# safe

> Un CLI pentru a interacționa cu seiful HashiCorp.
> Mai multe informaţii: <https://github.com/starkandwayne/safe>

- Adaugă o ţintă sigură:

`safe target {{vault_addr}} {{target_name}}`

- Autentificați clientul CLI împotriva serverului Vault, utilizând un simbol de autentificare:

`safe auth {{authentication_token}}`

- Tipăriţi variabilele de mediu care descriu ţinta curentă:

`safe env`

- Afișează o ierarhie de arbori a tuturor tastelor accesibile pentru o anumită cale:

`safe tree {{path}}`

- Mutați un secret de la o cale la alta:

`safe move {{old/path/to/secret}} {{new/path/to/secret}}`

- Generați o nouă pereche de chei SSH 2048-bit și păstrați-l:

`safe ssh {{2048}} {{path/to/secret}}`

- Setați chei nesensibile pentru un secret:

`safe set {{path/to/secret}} {{key}}={{value}}`

- Setați parola generată automat într-un secret:

`safe gen {{path/to/secret}} {{key}}`
