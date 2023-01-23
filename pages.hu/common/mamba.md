# mamba

> Gyors, platformokon átívelő csomagkezelő, amely a conda helyettesítésére szolgál. Néhány alparancsnak, mint például a `mamba repoquery`, saját használati dokumentációja van. További információ: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html>.

- Új környezet létrehozása, a megadott csomagok telepítésével:

`mamba create --name {{environment_name}} {{python=3.10 matplotlib}}`

- Csomagok telepítése az aktuális környezetbe, a csomag \[c\]hannel megadásával:

`mamba install -c {{conda-forge}} {{python=3.6 numpy}}`

- Az aktuális környezet összes csomagjának frissítése:

`mamba update --all`

- Egy adott csomag keresése a tárolók között:

`mamba repoquery search {{numpy}}`

- Az összes környezet listázása:

`mamba info --envs`

- A nem használt \[p\]ackage-ok és \[t\]arballok eltávolítása a gyorsítótárból:

`mamba clean -pt`

- Környezet aktiválása:

`mamba activate {{environment_name}}`

- Az aktuálisan aktivált környezet összes telepített csomagjának listázása:

`mamba list`
