# atom

> Editor teks yang dapat dipasang lintas platform.
> Plugin dikelola oleh `apm`.
> Catatan: Dukungan aplikasi Atom telah ditutup dan tidak lagi dikelola secara aktif.
> Informasi lebih lanjut: <https://atom.io/>.

- Buka suatu berkas atau direktori:

`atom {{jalan/menuju/berkas_atau_direktori}}`

- Buka berkas atau direktori dalam jendela baru:

`atom -n {{jalan/menuju/berkas_atau_direktori}}`

- Buka berkas atau direktori di jendela yang sudah ada:

`atom --add {{jalan/menuju/berkas_atau_direktori}}`

- Buka Atom dalam mode aman (tidak memuat paket plugin tambahan apa pun):

`atom --safe`

- Jalankan Atom sebagai subproses pada sesi terminal saat ini, jangan memuat Atom sebagai proses latar belakang:

`atom --foreground`

- Tunggu jendela Atom untuk ditutup sebelum kembali ke sesi terminal saat ini (berguna untuk editor komit Git):

`atom --wait`
