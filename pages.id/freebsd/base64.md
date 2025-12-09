# base64

> Lakukan pengodean dan pendekodean terhadap suatu berkas atau `stdin` dari/menuju format Base64, menuju `stdout` atau berkas lainnya.
> Informasi lebih lanjut: <https://man.freebsd.org/cgi/man.cgi?query=base64>.

- Kodekan isi suatu berkas menuju format Base64, dan keluarkan hasil menuju `stdout`:

`base64 {{[-i|--input]}} {{jalan/menuju/berkas}}`

- Kodekan isi suatu berkas menuju format Base64, dan keluarkan hasil menuju suatu berkas luaran/output:

`base64 {{[-i|--input]}} {{jalan/menuju/berkas_input}} {{[-o|--output]}} {{jalan/menuju/berkas_output}}`

- Bungkus luaran Base64 dalam panjang karakter yang tetap (nilai `0` akan menonaktifkan pembungkusan):

`base64 {{[-b|--break]}} {{0|76|...}} {{jalan/menuju/berkas}}`

- Dekodekan kode Base64 yang tersimpan dalam suatu berkas, dan keluarkan hasil menuju `stdout`:

`base64 {{[-d|--decode]}} {{[-i|--input]}} {{jalan/menuju/berkas}}`

- Kodekan isi dari `stdin` menuju `stdout`:

`{{perintah}} | base64`

- Dekodekan kode Base64 yang berasal dari `stdin` menuju `stdout`:

`{{perintah}} | base64 {{[-d|--decode]}}`
