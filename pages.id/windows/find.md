# find

> Mencari teks tertentu di dalam suatu file atau direktori.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- Mencari baris-baris dalam file yang mengandung teks tertentu:

`find {{teks}} {{jalan/menuju/file_atau_direktori}}`

- Menunjukkan baris-baris dalam file yang tidak mengandung teks tertentu:

`find {{teks}} {{jalan/menuju/file_atau_direktori}} /v`

- Menghitung jumlah baris dalam file yang mengandung teks tertentu:

`find {{teks}} {{jalan/menuju/file_atau_direktori}} /c`

- Mencari baris-baris dalam file yang mengandung teks tertentu beserta nomor barisnya:

`find {{teks}} {{jalan/menuju/file_atau_direktori}} /n`
