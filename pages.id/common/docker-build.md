# docker build

> Bangun sebuah image dari Dockerfile.
> Informasi lebih lanjut: <https://docs.docker.com/engine/reference/commandline/build/>.

- Bangun sebuah image docker meggunakan Dockerfile dalam direktori saat ini:

`docker build .`

- Bangun sebuah docker image dari Dockerfile dengan menggunakan URL yang spesifik:

`docker build {{github.com/creack/docker-firefox}}`

- Bangun sebuah docker image dengan tag tertentu:

`docker build --tag {{nama:tag}} .`

- Bangun sebuah docker image tanpa konteks pembangunan:

`docker build --tag {{nama:tag}} - < {{Dockerfile}}`

- Bangun sebuah image tanpa menggunakan cache:

`docker build --no-cache --tag {{nama:tag}} .`

- Bangun sebuah docker image dengan Dockerfile tertentu:

`docker build --file {{Dockerfile}} .`

- Bangun sebuah docker image dengan variabel lingkungan tertentu:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
