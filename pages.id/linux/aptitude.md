# aptitude

> Alat manajer paket piranti lunak Ubuntu dan Debian.
> Informasi lebih lanjut: <https://manned.org/aptitude>.

- Padankan seluruh informasi daftar paket dan versi yang tersedia. Perintah ini seharusnya dijalankan terlebih dahulu sebelum memasukkan perintah `aptitude` lainnya:

`sudo aptitude update`

- Pasang baru suatu paket beserta ketergantungannya:

`sudo aptitude install {{paket}}`

- Cari untuk suatu paket:

`aptitude search {{paket}}`

- Cari untuk paket yang telah terpasang: (`?installed` adalah kata kunci pencarian dalam `aptitude`):

`aptitude search '?installed({{paket}})'`

- Hapus suatu paket beserta seluruh ketergantungannya:

`sudo aptitude remove {{paket}}`

- Mutakhirkan seluruh paket yang telah terpasang menuju versi terbaru bila tersedia:

`sudo aptitude upgrade`

- Mutakhirkan seluruh paket (layaknya `aptitude upgrade`) serta buang paket-paket yang sudah tak terpakai dan pasang paket tambahan untuk memenuhi syarat ketergantungan paket yang terbaru:

`sudo aptitude full-upgrade`

- Masukkan suatu paket terpasang ke dalam daftar penahanan sehingga tidak boleh diperbarui secara otomatis:

`sudo aptitude hold '?installed({{paket}})'`
