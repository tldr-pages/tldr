# cmd

> Penerjemah baris perintah Windows.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Jalankan suatu sesi syel interaktif:

`cmd`

- Jalankan suatu perintah ([c]ommand):

`cmd /c {{echo Halo dunia}}`

- Jalankan kumpulan perintah dalam suatu berkas skrip:

`cmd {{jalan\menuju\skrip.bat}}`

- Jalankan kumpulan perintah spesifik dan kemudian jalankan suatu sesi syel interaktif:

`cmd /k {{echo Halo dunia}}`

- Jalankan suatu sesi syel interaktif di mana fungsi `echo` dimatikan dalam luaran perintah:

`cmd /q`

- Jalankan suatu sesi shell interaktif dengan mengaktifkan atau menonaktifkan fitur ekspansi [v]ariabel tertunda:

`cmd /v:{{on|off}}`

- Jalankan suatu sesi shell interaktif dengan mengaktifkan atau menonaktifkan fitur [e]kstensi perintah:

`cmd /e:{{on|off}}`

- Jalankan suatu sesi shell interaktif dengan menggunakan [u]nicode sebagai metode pengkodean luaran teks:

`cmd /u`
