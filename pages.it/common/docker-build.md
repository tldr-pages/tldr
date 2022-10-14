# docker build

> Crea un'immagine a partire da un Dockerfile. La creazione di un'immagine docker è chiamata build.
> Maggiori informazioni: <https://docs.docker.com/engine/reference/commandline/build/>.

- Crea un'immagine docker usando il Dockerfile nella cartella corrente:

`docker build .`

- Crea un'immagine docker usando il Dockerfile disponibile a un dato URL:

`docker build {{github.com/creack/docker-firefox}}`

- Crea e tagga un'immagine docker:

`docker build --tag {{nome:tag}} .`

- Non usare la cache per la creazione di un'immagine docker:

`docker build --no-cache --tag {{nome:tag}} .`

- Crea un'immagine docker usando un dato Dockerfile:

`docker build --file {{Dockerfile}} .`

- Crea un'immagine docker usando variabili fornite in fase di build:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
