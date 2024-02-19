# docker

> Atur kontainer Docker dan image.
> Kami mempunyai dokumentasi terpisah untuk menggunakan subperintah seperti `docker run`.
> Informasi lebih lanjut: <https://docs.docker.com/engine/reference/commandline/cli/>.

- Tampilkan semua daftar kontainer docker (yang sedang berjalan dan berhenti):

`docker ps --all`

- Nyalakan sebuah kontainer dari citra (image), dengan nama kustom:

`docker run --name {{nama_kontainer}} {{citra}}`

- Nyalakan atau menghentikan kontainer yang tersedia:

`docker {{start|stop}} {{nama_kontainer}}`

- Tarik citra dari registri docker:

`docker pull {{citra}}`

- Tampilkan daftar citra Docker yang telah diunduh:

`docker images`

- Buka sesi shell didalam sebuah kontainer yang sedang berjalan:

`docker exec -it {{nama_kontainer}} {{sh}}`

- Hapus kontainer yang sedang berhenti:

`docker rm {{nama_kontainer}}`

- Ambil dan ikuti semua log dari sebuah kontainer:

`docker logs -f {{nama_kontainer}}`
