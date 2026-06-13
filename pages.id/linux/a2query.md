# a2query

> Dapatkan konfigurasi yang dipakai saat ini (secara runtime) dari piranti peladen Apache dalam sistem operasi berbasis Debian.
> Informasi lebih lanjut: <https://manned.org/a2query>.

- Tampilkan daftar modul Apache yang sedang aktif:

`sudo a2query -m`

- Cek apakah suatu modul Apache sedang aktif:

`sudo a2query -m {{nama_modul}}`

- Tampilkan daftar host maya (virtual hosts) yang sedang aktif:

`sudo a2query -s`

- Tampilkan jenis modul Multi Processing Module yang sedang aktif:

`sudo a2query -M`

- Tampilkan versi piranti peladen Apache:

`sudo a2query -v`
