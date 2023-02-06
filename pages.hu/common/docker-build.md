# docker build

> Kép készítése egy Docker-fájlból. További információ: <https://docs.docker.com/engine/reference/commandline/build/>.

- Docker-kép készítése az aktuális könyvtárban lévő Dockerfile segítségével:

`docker build .`

- Docker-kép építése egy megadott URL-cím alatt található Dockerfile-ból:

`docker build {{github.com/creack/docker-firefox}}`

- Docker image építése és címkézése:

`docker build --tag {{name:tag}} .`

- Docker image építése építési kontextus nélkül:

`docker build --tag {{name:tag}} - < {{Dockerfile}}`

- Ne használja a gyorsítótárat az image építése során:

`docker build --no-cache --tag {{name:tag}} .`

- Docker image építése egy adott Dockerfile felhasználásával:

`docker build --file {{Dockerfile}} .`

- Építés egyéni build-time változókkal:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
