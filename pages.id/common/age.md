# age

> Alat pengenkripsi file yang sederhana, modern, dan aman.
> Lihat juga: `age-keygen`.
> Informasi lebih lanjut: <https://github.com/FiloSottile/age#usage>.

- Buat sebuah file terenkripsi yang hanya dapat didekripsi menggunakan kata sandi:

`age --passphrase --output {{jalan/menuju/berkas_terenkripsi}} {{jalan/menuju/berkas_tidak_terenkripsi}}`

- Buat file terenkripsi dengan kunci publik (public key) secara literal (ulangi argumen `--recipient` untuk memberikan kunci publik tambahan):

`age --recipient {{kunci_publik}} --output {{jalan/menuju/berkas_terenkripsi}} {{jalan/menuju/berkas_tidak_terenkripsi}}`

- Buat file terenkripsi bagi para penerima menurut kunci-kunci publik mereka yang disimpan di dalam suatu file (satu kunci per baris):

`age --recipients-file {{path/to/file_daftar_penerima}} --output {{jalan/menuju/berkas_terenkripsi}} {{jalan/menuju/berkas_tidak_terenkripsi}}`

- Buka file terenkripsi dengan kata sandi:

`age --decrypt --output {{path/to/file_bebas_enkripsi}} {{jalan/menuju/berkas_terenkripsi}}`

- Buka file terenkripsi dengan kunci privat:

`age --decrypt --identity {{path/to/file_kunci_privat}} --output {{path/to/file_bebas_enkripsi}} {{jalan/menuju/berkas_terenkripsi}}`
