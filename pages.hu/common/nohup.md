# nohup

> Lehetővé teszi, hogy egy folyamat életben maradjon, amikor a terminál megölik. További információ: <https://www.gnu.org/software/coreutils/nohup>.

- Olyan folyamat futtatása, amely a terminálon túl is élhet:

`nohup {{command}} {{argument1 argument2 ...}}`

- Indítsa el a `nohup` oldalt háttérben:

`nohup {{command}} {{argument1 argument2 ...}} &`

- A terminálon túl is élni képes héjszkript futtatása:

`nohup {{path/to/script.sh}} &`

- Folyamat futtatása és a kimenet írása egy adott fájlba:

`nohup {{command}} {{argument1 argument2 ...}} > {{path/to/output_file}} &`
