# docker image

> Atur kumpulan citra Docker.
> Lihat juga: `docker build`, `docker image pull`, `docker image rm`.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/image/>.

- Tampilkan daftar citra Docker yang terpasang dalam lokal:

`docker {{[images|image ls]}}`

- Hapus citra Docker lokal yang tidak terpakai:

`docker image prune`

- Hapus seluruh citra yang tidak terpakai (tidak hanya kumpulan citra tanpa tag):

`docker image prune {{[-a|--all]}}`

- Tampilkan riwayat suatu citra Docker:

`docker {{[history|image history]}} {{citra}}`
