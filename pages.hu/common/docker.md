# docker

> Docker-konténerek és -képek kezelése. Néhány alparancsnak, mint például a `docker run`, saját használati dokumentációja van. További információ: [https://docs.docker.com/engine/reference/commandline/cli/.](https://docs.docker.com/engine/reference/commandline/cli/)

- Az összes (futó és leállított) docker konténer listázása:

`docker ps --all`

- Konténer indítása egy image-ből, egyéni névvel:

`docker run --name {{container_name}} {{image}}`

- Egy meglévő konténer indítása vagy leállítása:

`docker {{start|stop}} {{container_name}}`

- Egy image lehívása a docker registryből:

`docker pull {{image}}`

- A már letöltött image-ek listájának megjelenítése:

`docker images`

- Shell megnyitása egy futó konténeren belül:

`docker exec -it {{container_name}} {{sh}}`

- Egy leállított konténer eltávolítása:

`docker rm {{container_name}}`

- Egy konténer naplóinak lekérése és követése:

`docker logs -f {{container_name}}`
