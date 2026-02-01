# age

> Alat pengenkripsi berkas yang sederhana, modern, dan aman.
> Lihat juga: `age-keygen`.
> Informasi lebih lanjut: <https://github.com/FiloSottile/age#usage>.

- Buat sebuah berkas terenkripsi yang hanya dapat didekripsi menggunakan kata sandi:

`age {{[-p|--passphrase]}} {{[-o|--output]}} {{jalan/menuju/berkas_terenkripsi}} {{jalan/menuju/berkas_tidak_terenkripsi}}`

- Buat berkas terenkripsi dengan kunci publik (public key) secara literal (ulangi argumen `--recipient` untuk memberikan kunci publik tambahan):

`age {{[-r|--recipient]}} {{kunci_publik}} {{[-o|--output]}} {{jalan/menuju/berkas_terenkripsi}} {{jalan/menuju/berkas_tidak_terenkripsi}}`

- Buat berkas terenkripsi bagi para penerima menurut kunci-kunci publik mereka yang disimpan di dalam suatu berkas (satu kunci per baris):

`age {{[-R|--recipients-file]}} {{path/to/berkas_daftar_penerima}} {{[-o|--output]}} {{jalan/menuju/berkas_terenkripsi}} {{jalan/menuju/berkas_tidak_terenkripsi}}`

- Buka berkas terenkripsi dengan kata sandi:

`age {{[-d|--decrypt]}} {{[-o|--output]}} {{path/to/berkas_bebas_enkripsi}} {{jalan/menuju/berkas_terenkripsi}}`

- Buka berkas terenkripsi dengan kunci privat:

`age {{[-d|--decrypt]}} {{[-i|--identity]}} {{path/to/berkas_kunci_privat}} {{[-o|--output]}} {{path/to/berkas_bebas_enkripsi}} {{jalan/menuju/berkas_terenkripsi}}`
