# base32

> Lakukan pengodean dan pendekodean terhadap suatu berkas atau `stdin` dari/menuju format Base32, menuju `stdout`.
> Informasi lebih lanjut: <https://manned.org/base32>.

- Kodekan isi suatu berkas menuju format Base32:

`base32 {{jalan/menuju/berkas}}`

- Bungkus luaran Base32 dalam panjang karakter yang tetap (nilai `0` akan menonaktifkan pembungkusan):

`base32 {{[-w|--wrap]}} {{0|76|...}} {{jalan/menuju/berkas}}`

- Dekodekan kode Base32 yang tersimpan dalam suatu berkas:

`base32 {{[-d|--decode]}} {{jalan/menuju/berkas}}`

- Kodekan isi dari `stdin`:

`{{perintah}} | base32`

- Dekodekan kode Base32 yang berasal dari `stdout`:

`{{perintah}} | base32 {{[-d|--decode]}}`
