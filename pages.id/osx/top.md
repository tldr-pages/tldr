# top

> Tampilkan informasi waktu nyata dinamis tentang proses yang berjalan.
> Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/top.1.html>.

- Jalankan `top`, dan seluruh opsi akan tersedia dalam tampilan antarmuka:

`top`

- Jalankan `top` dengan mengurutkan daftar proses berdasarkan jumlah memori internal yang terpakai (urutan default - nomor induk proses):

`top -o mem`

- Jalankan `top` dengan mengurutkan daftar proses berdasarkan intensitas pemakaian CPU, kemudian waktu jalan program tersebut:

`top -o cpu -O time`

- Jalankan `top` dengan hanya menampilkan kumpulan proses yang dipunyai oleh suatu pengguna:

`top -user {{nama_pengguna}}`

- Tampilkan bantuan mengenai perintah-perintah interaktif:

`<?>`
