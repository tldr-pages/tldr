# chkdsk

> Memeriksa dan mencari kesalahan dalam sebuah sistem file dan metadata volume penyimpanan.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Memeriksa sebuah ruang penyimpanan berdasarkan huruf drive (diakhiri dengan titik dua), lokasi pemasangan, atau nama ruang:

`chkdsk {{ruang_penyimpanan}}`

- Memperbaiki kesalahan pada ruang penyimpanan yang ditentukan:

`chkdsk {{ruang_penyimpanan}} /f`

- Melepas ruang penyimpanan tertentu untuk pemeriksaan:

`chkdsk {{ruang_penyimpanan}} /x`

- Mengubah ukuran file log dalam sebuah ruang penyimpanan dengan sistem file NTFS:

`chkdsk /l{{ukuran}}`
