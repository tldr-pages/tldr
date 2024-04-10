# svcs

> Ambil atau atur sumber daya dari proses, tugas dan projek yang berjalan.
> Informasi lebih lanjut: <https://www.unix.com/man-page/linux/1/svcs>.

- Daftar semua servis yang berjalan:

`svcs`

- Daftar servis-servis yang tidak berjalan:

`svcs -vx`

- Daftar informasi tentang sebuah servis:

`svcs apache`

- Tampilkan lokasi dari berkas catatan servis:

`svcs -L apache`

- Display end of a service log file:

`tail $(svcs -L apache)`
