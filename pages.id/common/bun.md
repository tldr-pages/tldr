# bun

> Runtime dan alat program JavaScript.
> Memiliki pengemas (bundler), penguji, dan manajer paket bagi program.
> Informasi lebih lanjut: <https://bun.com/docs>.

- Buat sebuah proyek Bun baru dalam direktori saat ini:

`bun init`

- Jalankan suatu berkas JavaScript atau skrip yang terdaftar pada `package.json`:

`bun run {{jalan/menuju/berkas|nama_skrip}}`

- Jalankan pengujian unit (unit test):

`bun test`

- Unduh dan pasang seluruh paket yang terdaftar sebagai ketergantungan proyek dalam `package.json`:

`bun {{[i|install]}}`

- Tambahkan suatu dependensi ke dalam `package.json`:

`bun {{[a|add]}} {{nama_modul}}`

- Hapus suatu ketergantungan dari `package.json`:

`bun {{[rm|remove]}} {{nama_modul}}`

- Jalankan sebuah REPL (shell interaktif):

`bun repl`

- Perbarui Bun menuju versi terkini:

`bun upgrade`
