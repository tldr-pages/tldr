# docker build

> Construiți o imagine dintr-un fișier Dockerfile.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/build/>

- Construiți o imagine docker utilizând fișierul Dockerfile din directorul curent:

`docker build .`

- Construiți o imagine docker dintr-un fișier Dockerfile la un URL specificat:

`docker build {{github.com/creack/docker-firefox}}`

- Construiți o imagine docker și etichetați-o:

`docker build --tag {{name:tag}} .`

- Construiți o imagine docker fără context de construire:

`docker build --tag {{name:tag}} - < {{Dockerfile}}`

- Nu utilizați memoria cache atunci când construiți imaginea:

`docker build --no-cache --tag {{name:tag}} .`

- Construiește o imagine docker folosind un fișier Dockerfile specific:

`docker build --file {{Dockerfile}} .`

- Construiți cu variabile personalizate pentru timpul de construire:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
