# docker image rm

> Hapus kumpulan citra yang dikelola Docker.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Hapus satu atau beberapa citra berdasarkan nama masing-masing:

`docker {{[rmi|image rm]}} {{citra1 citra2 ...}}`

- Hapus suatu citra secara paksa:

`docker {{[rmi|image rm]}} {{[-f|--force]}} {{citra}}`

- Hapus suatu citra tanpa menghapus citra induk yang tak diberi tag:

`docker {{[rmi|image rm]}} --no-prune {{citra}}`

- Tampilkan bantuan:

`docker {{[rmi|image rm]}} --help`
