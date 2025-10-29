# wmic

> Syel interaktif untuk menampilkan informasi terperinci tentang kumpulan proses Windows yang berjalan.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/wmic>.

- Tata bahasa dasar perintah:

`wmic {{alias}} {{klausa_di_mana}} {{klausa_kata_kerja}}`

- Tampilkan informasi seluruh proses yang sedang berjalan secara ringkas:

`wmic process list brief`

- Tampilkan informasi seluruh proses yang sedang berjalan secara rinci:

`wmic process list full`

- Dapatkan data kolom spesifik seperti nama prosess, nomor induk (ID), dan nomor induk proses induk:

`wmic process get {{name,processid,parentprocessid}}`

- Tampilkan informasi tentang suatu proses:

`wmic process where {{name="example.exe"}} list full`

- Tampilkan data kolom-kolom spesifik terhadap suatu proses:

`wmic process where processid={{pid}} get {{name,commandline}}`

- Bunuh suatu proses:

`wmic process {{pid}} delete`
