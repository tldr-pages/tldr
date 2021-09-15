# docker

> Mengatur kontainer Docker dan image.
> Kami mempunyai dokumentasi terpisah untuk menggunakan subperintah seperti `docker run`.
> Informasi lebih lanjut: <https://docs.docker.com/engine/reference/commandline/cli/>.

- Menampilkan semua daftar kontainer docker yang sedang berjalan:

`docker ps`

- Menampilkan semua daftar kontainer docker (yang sedang berjalan dan berhenti):

`docker ps -a`

- Memulai sebuah kontainer dari image, dengan nama kustom:

`docker run --name {{nama_kontainer}} {{image}}`

- Memulai atau menghentikan kontainer yang tersedia:

`docker {{start|stop}} {{nama_kontainer}}`

- Menarik image dari registri docker:

`docker pull {{image}}`

- Membuka shell didalam sebuah kontainer yang sedang berjalan:

`docker exec -it {{nama_kontainer}} {{sh}}`

- Menghapus kontainer yang sedang berhenti:

`docker rm {{nama_kontainer}}`

- Mengambil dan mengikuti semua log dari sebuah kontainer:

`docker logs -f {{nama_kontainer}}`
