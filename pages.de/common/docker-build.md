# docker build

> Baut ein Image aus einem Dockerfile.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/buildx/build/>.

- Baue ein Docker Image aus dem Dockerfile im aktuellen Verzeichnis:

`docker build .`

- Baue ein Docker Image aus einem Dockerfile an einer angegebenen URL:

`docker build {{github.com/creack/docker-firefox}}`

- Baue ein Docker Image und gib ihm einen Tag:

`docker build {{[-t|--tag]}} {{name:tag}} .`

- Baue ein Docker Image ohne Build-Kontext:

`docker build {{[-t|--tag]}} {{name:tag}} - < {{Dockerfile}}`

- Verwende keinen Cache beim Bauen des Docker Images:

`docker build --no-cache {{[-t|--tag]}} {{name:tag}} .`

- Baue ein Docker Image mit einem spezifischen Dockerfile:

`docker build {{[-f|--file]}} {{Dockerfile}} .`

- Baue mit benutzerdefinierten Variablen, die während des Bauens zur Verfügung stehen:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
