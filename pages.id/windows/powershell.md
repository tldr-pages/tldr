# powershell

> Sebuah syel/shell dan bahasa pemrograman berbasis naskah/script yang dirancang untuk administrasi sistem komputer.
> Perintah ini merujuk kepada PowerShell versi 5.1 ke bawah (juga dikenal sebagai PowerShell bawaan Windows). Gunakan perintah `pwsh` daripada `powershell` untuk menggunakan PowerShell versi terkini (6.0 ke atas) yang tersedia lintas sistem operasi.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Jalankan sesi PowerShell interaktif baru:

`powershell`

- Jalankan sesi interaktif tanpa memuat profil konfigurasi startup:

`powershell -NoProfile`

- Jalankan perintah secara spesifik:

`powershell -Command "{{echo 'powershell telah dieksekusi'}}"`

- Jalankan suatu naskah perintah/script PowerShell:

`powershell -File {{jalan/menuju/naskah.ps1}}`

- Jalankan suatu sesi dengan versi PowerShell tertentu:

`powershell -Version {{versi}}`

- Cegah sesi PowerShell dari keluar secara otomatis setelah menjalankan perintah startup:

`powershell -NoExit`

- Tentukan format data yang akan dimasukkan ke dalam PowerShell:

`powershell -InputFormat {{Text|XML}}`

- Tentukan format data yang ingin dikeluarkan dari perintah-perintah PowerShell:

`powershell -OutputFormat {{Text|XML}}`
