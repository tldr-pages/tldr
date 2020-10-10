# docker

> Mengatur kontainer Docker dan image.
> Informasi selengkapnya: <https://docs.docker.com/engine/reference/commandline/cli/>.

- Menampilkan semua daftar kontainer docker yang sedang berjalan:

`docker ps`

- Menampilkan semua daftar kontainer docker (yang sedang berjalan dan berhenti):

`docker ps -a`

- Memulai sebuah kontainer dari image, dengan nama kustom:

`docker run --name {{container_name}} {{image}}`

- Memulai atau menghentikan kontainer yang tersedia:

`docker {{start|stop}} {{container_name}}`

- Menarik image dari registri docker:

`docker pull {{image}}`

- Membuka shell didalam sebuah kontainer yang sedang berjalan:

`docker exec -it {{container_name}} {{sh}}`

- Menghapus kontainer yang sedang berhenti:

`docker rm {{container_name}}`

- Mengambil dan mengikuti semua log dari sebuah kontainer:

`docker logs -f {{container_name}}`
