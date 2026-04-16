# dircolors

> Tampilkan perintah untuk mengatur variabel lingkungan `$LS_COLOR` dan pengayaan warna luaran program `ls`, `dir`, dsb.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>.

- Tampilkan perintah untuk menyetel nilai `$LS_COLOR` menggunakan skema warna bawaan:

`dircolors`

- Tampilkan setiap jenis berkas beserta pengaturan warna teks saat ditampilkan dalam `ls`:

`dircolors --print-ls-colors`

- Tampilkan perintah untuk menyetel `$LS_COLOR` menggunakan warna yang didefinisikan dalam suatu berkas:

`dircolors {{jalan/menuju/berkas}}`

- Tampilkan perintah versi Bourne shell:

`dircolors {{[-b|--bourne-shell]}}`

- Tampilkan perintah versi C shell:

`dircolors {{[-c|--c-shell]}}`

- Tampilkan informasi daftar warna untuk setiap jenis berkas dan ekstensi nama berkas:

`dircolors {{[-p|--print-database]}}`
