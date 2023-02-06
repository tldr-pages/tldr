# docker container

> Docker konténerek kezelése. További információ: <https://docs.docker.com/engine/reference/commandline/container/>.

- A jelenleg futó Docker konténerek listázása:

`docker container ls`

- Egy vagy több leállított konténer indítása:

`docker container start {{container1_name}} {{container2_name}}`

- Egy vagy több futó konténer leállítása:

`docker container kill {{container_name}}`

- Egy vagy több futó konténer leállítása:

`docker container stop {{container_name}}`

- Egy vagy több konténeren belüli összes folyamat szüneteltetése:

`docker container pause {{container_name}}`

- Egy vagy több konténer részletes információinak megjelenítése:

`docker container inspect {{container_name}}`

- Egy konténer fájlrendszerének exportálása tar-archívumként:

`docker container export {{container_name}}`

- Új image létrehozása egy konténer módosításaiból:

`docker container commit {{container_name}}`
