# asar

> Pengarsip berkas untuk platform Electron.
> Informasi lebih lanjut: <https://github.com/electron/asar>.

- Arsipkan sebuah berkas atau direktori:

`asar pack {{path/to/file_or_directory}} {{archived.asar}}`

- Mengekstrak sebuah arsip:

`asar extract {{archived.asar}}`

- Mengekstrak berkas tertentu dari sebuah arsip:

`asar extract-file {{archived.asar}} {{file}}`

- Mendapatkan daftar konten dari berkas arsip:

`asar list {{archived.asar}}`
