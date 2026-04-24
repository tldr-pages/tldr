# docker container start

> Jalankan kontainer-kontainer yang dihentikan.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/container/start/>.

- Jalankan suatu kontainer Docker:

`docker {{[start|container start]}} {{kontainer}}`

- Jalankan suatu kontainer, serta hubungkan hasil `stdout` dan `stderr`, beserta sinyal-sinyal input ke dalam kontainer:

`docker {{[start|container start]}} {{[-a|--attach]}} {{kontainer}}`

- Jalankan satu atau beberapa kontainer:

`docker {{[start|container start]}} {{kontainer1 kontainer2 ...}}`

- Tampilkan bantuan:

`docker {{[start|container start]}} --help`
