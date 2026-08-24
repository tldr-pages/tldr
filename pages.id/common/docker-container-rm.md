# docker container rm

> Hapus kontainer.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/container/rm/>.

- Hapus kumpulan kontainer:

`docker {{[rm|container rm]}} {{kontainer1 kontainer2 ...}}`

- Hapus dengan paksa:

`docker {{[rm|container rm]}} {{[-f|--force]}} {{kontainer1 kontainer2 ...}}`

- Hapus suatu kontainer beserta volumenya:

`docker {{[rm|container rm]}} {{[-v|--volumes]}} {{kontainer}}`

- Tampilkan bantuan:

`docker {{[rm|container rm]}} --help`
