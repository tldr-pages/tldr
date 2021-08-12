# secrethub

> Un instrument pentru a păstra secrete în afara fișierelor de configurare.
> Mai multe informaţii: <https://secrethub.io>

- Imprimați un secret pentru a stdout:

`secrethub read {{path/to/secret}}`

- Generați o valoare aleatoare și stocați ca un secret nou sau actualizat:

`secrethub generate {{path/to/secret}}`

- Stocați o valoare din clipboard ca un secret nou sau actualizat:

`secrethub write --clip {{path/to/secret}}`

- Stocați o valoare furnizată pe stdin ca un secret nou sau actualizat:

`echo "{{secret_value}}" | secrethub write {{path/to/secret}}`

- Audit un depozit sau un secret:

`secrethub audit {{path/to/repo_or_secret}}`
