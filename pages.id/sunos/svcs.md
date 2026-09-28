# svcs

> Ambil atau atur sumber daya dari proses, tugas dan projek yang berjalan.
> Informasi lebih lanjut: <https://www.unix.com/man-page/sunos/1/svcs>.

- Daftar semua servis yang berjalan:

`svcs`

- Daftar servis-servis yang tidak berjalan:

`svcs -vx`

- Daftar informasi tentang sebuah servis:

`svcs apache`

- Tampilkan lokasi dari berkas catatan servis:

`svcs -L apache`

- Tampilkan isi akhir suatu berkas log servis:

`tail $(svcs -L apache)`
