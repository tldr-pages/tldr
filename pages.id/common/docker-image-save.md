# docker image save

> Ekspor kumpulan citra Docker menuju berkas arsip.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/image/save/>.

- Simpan suatu citra dengan menangkap isi dari `stdout` menuju suatu berkas arsip `.tar`:

`docker {{[save|image save]}} {{citra}}:{{tag}} > {{jalan/menuju/berkas.tar}}`

- Simpan suatu citra menuju suatu arsip `.tar`:

`docker {{[save|image save]}} {{[-o|--output]}} {{jalan/menuju/berkas.tar}} {{image}}:{{tag}}`

- Simpan seluruh tag dalam proses ekspor citra:

`docker {{[save|image save]}} {{[-o|--output]}} {{jalan/menuju/berkas.tar}} {{nama_citra}}`

- Tentukan daftar tag yang hendak disimpan dalam proses ekspor citra:

`docker {{[save|image save]}} {{[-o|--output]}} {{jalan/menuju/berkas.tar}} {{nama_citra:tag1 nama_citra:tag2 ...}}`
