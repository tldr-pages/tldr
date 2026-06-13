# Get-Date

> Dapatkan tanggal dan waktu saat ini.
> Catatan: Perintah ini hanya dapat digunakan dalam PowerShell.
> Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-date>.

- Tampilkan tanggal dan waktu saat ini:

`Get-Date`

- Tampilkan tanggal dan waktu saat ini dengan format tanggal/waktu .NET:

`Get-Date -Format "{{yyyy-MM-dd HH:mm:ss}}"`

- Tampilkan tanggal dan waktu saat ini dalam zona waktu UTC dan format ISO 8601:

`(Get-Date).ToUniversalTime()`

- Ubah suatu nilai timestamp Unix:

`Get-Date -UnixTimeSeconds {{1577836800}}`
