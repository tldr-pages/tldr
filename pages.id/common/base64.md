# base64

> Lakukan pengodean dan pendekodean terhadap suatu berkas atau `stdin` dari/menuju format Base64, menuju `stdout`.
> Informasi lebih lanjut: <https://manned.org/base64>.

- Kodekan isi suatu berkas menuju format Base64:

`base64 {{jalan/menuju/berkas}}`

- Bungkus luaran Base64 dalam panjang karakter yang tetap (nilai `0` akan menonaktifkan pembungkusan):

`base64 {{[-w|--wrap]}} {{0|76|...}} {{jalan/menuju/berkas}}`

- Dekodekan kode Base64 yang tersimpan dalam suatu berkas:

`base64 {{[-d|--decode]}} {{jalan/menuju/berkas}}`

- Kodekan isi dari `stdin`:

`{{perintah}} | base64`

- Dekodekan kode Base64 yang berasal dari `stdout`:

`{{perintah}} | base64 {{[-d|--decode]}}`
