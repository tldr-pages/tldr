# makepkg

> Buat paket yang dapat digunakan dengan `pacman`.
> Menggunakan file `PKGBUILD` di direktori kerja saat ini secara default.
> Informasi lebih lanjut: <https://manned.org/makepkg.8>.

- Membuat paket:

`makepkg`

- Buat paket dan instal dependensinya:

`makepkg {{[-s|--syncdeps]}}`

- Buat paket dan instal dependensinya lalu instal ke dalam sistem:

`makepkg {{[-si|--syncdeps --install]}}`

- Buat paket, namun lewati pemeriksaan sumber hash:

`makepkg --skipchecksums`

- Bersihkan direktori kerja setelah pembuatan berhasil:

`makepkg {{[-c|--clean]}}`

- Verifikasi sumber hash:

`makepkg --verifysource`

- Hasilkan dan simpan informasi sumber ke dalam `.SRCINFO`:

`makepkg --printsrcinfo > .SRCINFO`

- Unduh sumbernya dan instal hanya dependensi build untuk suatu program:

`makepkg {{[-so|--syncdeps --nobuild]}}`
