# base64

> Tulis ulang isi suatu berkas atau `stdin` dalam format biner dari/menuju format penulisan enkoding Base64, menuju `stdout`.
> Informasi lebih lanjut: <https://manned.org/base64>.

- Tulis ulang isi biner suatu berkas dalam format Base64:

`base64 {{jalan/menuju/berkas}}`

- Bungkus luaran Base64 dalam panjang karakter yang tetap (nilai `0` akan menonaktifkan pembungkusan):

`base64 {{[-w|--wrap]}} {{0|76|...}} {{jalan/menuju/berkas}}`

- Tulis ulang isi suatu berkas dari format Base64 menuju format asli/biner:

`base64 {{[-d|--decode]}} {{jalan/menuju/berkas}}`

- Tulis ulang isi biner `stdin` menuju format Base32:

`{{perintah}} | base64`

- Tulis ulang isi Base64 `stdin` menuju format asli/biner:

`{{perintah}} | base64 {{[-d|--decode]}}`
