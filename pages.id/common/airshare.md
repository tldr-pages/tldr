# airshare

> Pindahkan data antara dua perangkat dalam jaringan lokal yang sama.
> Informasi lebih lanjut: <https://airshare.rtfd.io/en/latest/cli.html>.

- Kirim kumpulan file atau direktori:

`airshare {{kode_berbagi}} {{jalan/menuju/file_atau_direktori1 jalan/menuju/file_atau_direktori2 ...}}`

- Terima file:

`airshare {{kode_berbagi}}`

- Nyalakan `airshare` sebagai server penerima (sehingga memungkingkan Anda untuk mengunggah melalui situs web internal):

`airshare --upload {{kode_berbagi}}`

- Unggah kumpulan file atau direktori menuju server penerima:

`airshare --upload {{kode_berbagi}} {{jalan/menuju/file_atau_direktori1 jalan/menuju/file_atau_direktori2 ...}}`

- Kirim file dengan alamat-alamat yang disalin pada papan klip (clipboard):

`airshare --file-path {{kode_berbagi}}`

- Terima dan salin file menuju papan klip:

`airshare --clip-receive {{kode_berbagi}}`
