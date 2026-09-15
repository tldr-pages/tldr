# basenc

> Tulis ulang isi suatu berkas atau `stdin` dalam format biner dari/menuju format penulisan enkoding tertentu, menuju `stdout`.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/basenc-invocation.html>.

- Tulis ulang isi biner suatu berkas dalam format Base64:

`basenc --base64 {{jalan/menuju/berkas}}`

- Tulis ulang isi suatu berkas dari format Base64 menuju format asli/biner:

`basenc {{[-d|--decode]}} --base64 {{jalan/menuju/berkas}}`

- Tulis ulang isi biner `stdin` menuju format Base32 dengan panjang baris 42 karakter:

`{{perintah}} | basenc --base32 {{[-w|--wrap]}} 42`

- Tulis ulang isi biner `stdin` menuju format Base32:

`{{perintah}} | basenc --base32`
