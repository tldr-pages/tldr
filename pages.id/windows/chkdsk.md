# chkdsk

> Memeriksa dan mencari kesalahan dalam sebuah sistem file dan metadata volume penyimpanan.
> Informasi lebih lanjut: <https://docs.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Memeriksa sebuah volume penyimpanan berdasarkan huruf drive (diakhiri dengan titik dua), lokasi pemasangan, atau nama volume:

`chkdsk {{volume}}`

- Memperbaiki kesalahan pada volume penyimpanan yang ditentukan:

`chkdsk {{volume}} /f`

- Melepas volume penyimpanan tertentu untuk pemeriksaan:

`chkdsk {{volume}} /x`

- Mengubah ukuran file log dalam sebuah volume dengan sistem file NTFS:

`chkdsk /l{{ukuran}}`
