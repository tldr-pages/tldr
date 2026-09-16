# cmd

> Penerjemah baris perintah Windows.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Jalankan suatu sesi syel interaktif:

`cmd`

- Jalankan kumpulan perintah secara spesifik:

`cmd /c {{echo 'perintah cmd telah dijalankan'}}`

- Jalankan suatu naskah/skrip perintah:

`cmd {{jalan\menuju\skrip.bat}}`

- Jalankan kumpulan perintah spesifik dan kemudian jalankan suatu sesi syel interaktif:

`cmd /k {{echo 'perintah cmd telah dijalankan'}}`

- Jalankan suatu sesi syel interaktif di mana fungsi `echo` dimatikan dalam luaran perintah:

`cmd /q`

- Jalankan suatu sesi shell interaktif dengan mengaktifkan atau menonaktifkan fitur ekspansi [v]ariabel tertunda:

`cmd /v:{{on|off}}`

- Jalankan suatu sesi shell interaktif dengan mengaktifkan atau menonaktifkan fitur [e]kstensi perintah:

`cmd /e:{{on|off}}`

- Jalankan suatu sesi shell interaktif dengan menggunakan [u]nicode sebagai format penulisan luaran teks:

`cmd /u`
