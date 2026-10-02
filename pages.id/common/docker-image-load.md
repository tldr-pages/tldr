# docker image load

> Muat citra-citra Docker baik dari kumpulan berkas maupun `stdin`.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/image/load/>.

- Muat sebuah citra Docker dari `stdin`:

`docker < {{jalan/menuju/berkas_citra.tar}} {{[load|image load]}}`

- Muat sebuah citra Docker dari suatu berkas:

`docker {{[load|image load]}} {{[-i|--input]}} {{jalan/menuju/berkas_citra.tar}}`

- Muat sebuah citra Docker dari suatu berkas dalam mode sunyi:

`docker {{[load|image load]}} {{[-q|--quiet]}} {{[-i|--input]}} {{jalan/menuju/berkas_citra.tar}}`
