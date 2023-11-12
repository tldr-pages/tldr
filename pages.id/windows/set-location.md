# Set-Location

> Tampilkan direktori kerja saat ini atau pindah ke direktori lain.
> Perintah ini hanya dapat digunakan dalam PowerShell.
> Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- Pergi menuju suatu direktori pada drive yang sama:

`Set-Location {{jalan\menuju\direktori}}`

- Pergi menuju direktori tertentu pada [d]rive yang berbeda:

`Set-Location /d {{C}}:{{jalan\menuju\direktori}}`

- Pergi dan tampilkan lokasi lengkap (absolute path) atas direktori yang dituju:

`Set-Location {{jalan\menuju\direktori}} -PassThru`

- Pergi menuju induk dari direktori dari saat ini:

`Set-Location ..`

- Pergi menuju direktori pangkal/home milik pengguna saat ini:

`Set-Location ~`

- Pergi menuju direktori yang telah dikunjungi sebelumnya/setelahnya

`Set-Location {{-|+}}`

- Pergi menuju akar (root) dari drive saat ini:

`Set-Location \`
