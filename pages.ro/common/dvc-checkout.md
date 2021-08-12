# dvc checkout

> Verificați fișierele de date și directoarele din memoria cache.
> Mai multe informaţii: <https://dvc.org/doc/command-reference/checkout>

- Checkout cea mai recentă versiune a tuturor fișierelor țintă și directoarelor:

`dvc checkout`

- Checkout la cea mai recentă versiune a unui obiectiv specificat:

`dvc checkout {{target}}`

- Checkout o versiune specifică a unui obiectiv de la un alt comitet Git/tag/sucursală:

`git checkout {{commit_hash|tag|branch}} {{target}} && dvc checkout {{target}}`
