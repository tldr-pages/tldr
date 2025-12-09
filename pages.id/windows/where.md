# where

> Tampilkan lokasi kumpulan berkas yang memenuhi kriteria suatu pola pencarian alamat berkas.
> Lokasi pencarian default diatur sebagai direktori kerja saat ini beserta kumpulan alamat yang diatur dalam variabel lingkungan PATH.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/where>.

- Tampilkan daftar alamat berkas yang memenuhi pola pencarian alamat:

`where {{pola_pencarian}}`

- Tampilkan hasil pencarian termasuk ukuran dan tanggal berkas:

`where /T {{pola_pencarian}}`

- Lakukan hasil pencarian terhadap suatu direktori secara rekursif:

`where /R {{jalan\menuju\direktori}} {{pola_pencarian}}`

- Hanya kembalikan kode galat dari hasil pencarian tanpa menampilkan daftar alamat:

`where /Q {{pola_pencarian}}`
