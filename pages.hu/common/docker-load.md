# docker load

> Docker-képek betöltése fájlokból vagy a `stdin`. További információ: [https://docs.docker.com/engine/reference/commandline/load/.](https://docs.docker.com/engine/reference/commandline/load/)

- Docker-kép betöltése a `stdin`:

`docker load < {{path/to/image_file.tar}}`

- Docker-kép betöltése egy adott fájlból:

`docker load --input {{path/to/image_file.tar}}`

- Docker-kép betöltése egy adott fájlból csendes üzemmódban:

`docker load --quiet --input {{path/to/image_file.tar}}`
