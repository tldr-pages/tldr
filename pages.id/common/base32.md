# base32

> Tulis ulang isi suatu berkas atau `stdin` dalam format biner dari/menuju format penulisan enkoding Base32, menuju `stdout`.
> Informasi lebih lanjut: <https://manned.org/base32>.

- Tulis ulang isi biner suatu berkas dalam format Base32:

`base32 {{jalan/menuju/berkas}}`

- Bungkus luaran Base32 dalam panjang karakter yang tetap (nilai `0` akan menonaktifkan pembungkusan):

`base32 {{[-w|--wrap]}} {{0|76|...}} {{jalan/menuju/berkas}}`

- Tulis ulang isi suatu berkas dari format Base32 menuju format asli/biner:

`base32 {{[-d|--decode]}} {{jalan/menuju/berkas}}`

- Tulis ulang isi biner `stdin` menuju format Base32:

`{{perintah}} | base32`

- Tulis ulang isi Base32 `stdin` menuju format asli/biner:

`{{perintah}} | base32 {{[-d|--decode]}}`
