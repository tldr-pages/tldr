# ffsend

> Bagikan berkas-berkas secara mudah dan aman.
> Informasi lebih lanjut: <https://gitlab.com/timvisee/ffsend>.

- Unggah suatu berkas:

`ffsend upload {{jalan/menuju/berkas}}`

- Unduh suatu berkas:

`ffsend download {{url}}`

- Unggah berkas dengan suatu kata sandi:

`ffsend upload {{jalan/menuju/berkas}} {{[-p|--password]}} {{kata_sandi}}`

- Unduh berkas yang terlindungi dengan suatu kata sandi:

`ffsend download {{url}} {{[-p|--password]}} {{kata_sandi}}`

- Unggah dan atur unggahan supaya hanya dapat diunduh sebanyak 4 kali:

`ffsend upload {{jalan/menuju/berkas}} {{[-d|--downloads]}} {{4}}`
