# conda

> Csomag-, függőség- és környezetkezelés bármilyen programozási nyelvhez. Néhány alparancsnak, mint például a `conda create`, saját használati dokumentációja van. További információ: <https://github.com/conda/conda>.

- Új környezet létrehozása, nevesített csomagok telepítése:

`conda create --name {{environment_name}} {{python=3.9 matplotlib}}`

- Az összes környezet listázása:

`conda info --envs`

- Környezet betöltése:

`conda activate {{environment_name}}`

- Egy környezet kitöltése:

`conda deactivate`

- Környezet törlése (minden csomag eltávolítása):

`conda remove --name {{environment_name}} --all`

- Csomagok telepítése az aktuális környezetbe:

`conda install {{python=3.4 numpy}}`

- Az aktuálisan telepített csomagok listája az aktuális környezetben:

`conda list`

- Fel nem használt csomagok és gyorsítótárak törlése:

`conda clean --all`
