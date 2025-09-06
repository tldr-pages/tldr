# calibre-server

> Suatu aplikasi peladen (server) untuk membagikan buku digital (e-book) dalam jaringan.
> Catatan: buku-buku digital harus sebelumnya diimpor menuju perpustakaan baik melalui aplikasi GUI maupun perintah `calibredb`.
> Bagian dari aplikasi perpustakaan buku digital Calibre.
> Informasi lebih lanjut: <https://manual.calibre-ebook.com/generated/en/calibre-server.html>.

- Jalankan peladen untuk berbagi buku digital. Akses perpustakaan pada <http://localhost:8080>:

`calibre-server`

- Jalankan peladen pada port berbeda. Akses perpustakaan pada <http://localhost:port>:

`calibre-server --port {{port}}`

- Lindungi peladen dengan membutuhkan kata sandi (password) untuk mengaksesnya:

`calibre-server --username {{nama_pengguna}} --password {{kata_sandi}}`
