# Get-FileHash

> Hitung hasil persandian hash (checksum) untuk suatu berkas.
> Catatan: Perintah ini hanya dapat digunakan dalam PowerShell.
> Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>.

- Hitung hash atas suatu berkas menggunakan algoritma SHA256:

`Get-FileHash {{jalan\menuju\berkas}}`

- Hitung hash atas suatu berkas menggunakan algoritma tertentu:

`Get-FileHash {{jalan\menuju\berkas}} -Algorithm {{SHA1|SHA384|SHA256|SHA512|MD5}}`

- Hitung hash atas suatu berkas menggunakan algoritma usang tertentu (tidak tersedia dalam PowerShell versi 6 ke atas):

`Get-FileHash {{jalan\menuju\berkas}} -Algorithm {{SHA1|SHA384|SHA256|SHA512|MD5}}`

- Periksa keabsahan isi suatu berkas dengan nilai hash yang diketahui:

`(Get-FileHash {{jalan\menuju\berkas}} -Algorithm {{SHA1|SHA256|SHA384|SHA512|MD5}}).Hash -eq "{{nilai_hash_blake2_yang_diketahui}}"`
