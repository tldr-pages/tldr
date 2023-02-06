# conda create

> Új conda környezetek létrehozása. További információ: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- Hozzon létre egy új környezetet `py39` néven, és telepítse bele a Python 3.9-et és a NumPy v1.11-et vagy magasabb verziószámú változatot:

`conda create --yes --name {{py39}} python={{3.9}} "{{numpy>=1.11}}"`

- Készítsen pontos másolatot egy környezetről:

`conda create --clone {{py39}} --name {{py39-copy}}`

- Új környezet létrehozása megadott névvel, és egy adott csomag telepítése:

`conda create --name {{env_name}} {{package_name}}`
