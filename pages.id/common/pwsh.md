# pwsh

> Sebuah syel/shell dan bahasa pemrograman berbasis naskah/script yang dirancang untuk administrasi sistem komputer.
> Perintah ini merujuk kepada PowerShell versi 6 ke atas (juga dikenal sebagai PowerShell Core dan PowerShell lintas sistem operasi). Gunakan perintah `powershell` daripada `pwsh` untuk menggunakan PowerShell versi bawaan Windows (5.1 ke bawah).
> Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>.

- Jalankan sesi PowerShell interaktif baru:

`pwsh`

- Jalankan sesi interaktif tanpa memuat profil konfigurasi startup:

`pwsh -NoProfile`

- Jalankan perintah secara spesifik:

`pwsh -Command "{{echo 'powershell telah dieksekusi'}}"`

- Jalankan suatu naskah perintah/script PowerShell:

`pwsh -File {{jalan/menuju/naskah.ps1}}`

- Jalankan suatu sesi dengan versi PowerShell tertentu:

`pwsh -Version {{versi}}`

- Cegah sesi PowerShell dari keluar secara otomatis setelah menjalankan perintah startup:

`pwsh -NoExit`

- Tentukan format data yang akan dimasukkan ke dalam PowerShell:

`pwsh -InputFormat {{Text|XML}}`

- Tentukan format data yang ingin dikeluarkan dari perintah-perintah PowerShell:

`pwsh -OutputFormat {{Text|XML}}`
