# Get-FileHash

> Hitung hasil persandian hash untuk suatu berkas.
> Catatan: Perintah ini hanya dapat digunakan dalam PowerShell.
> Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>.

- Hitung hash atas suatu berkas menggunakan algoritma SHA256:

`Get-FileHash {{jalan\menuju\berkas}}`

- Hitung hash atas suatu berkas menggunakan algoritma tertentu:

`Get-FileHash {{jalan\menuju\berkas}} -Algorithm {{SHA1|SHA384|SHA256|SHA512|MD5}}`
