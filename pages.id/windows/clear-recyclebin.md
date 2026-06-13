# Clear-RecycleBin

> Bersihkan berkas dari Keranjang Sampah (Recycle Bin).
> Perintah ini hanya dapat dijalankan dalam PowerShell versi 5.1 dan ke bawah, atau 7.1 ke atas.
> Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/clear-recyclebin>.

- Bersihkan dan hapus seluruh berkas dari Keranjang Sampah:

`Clear-RecycleBin`

- Hapus berkas dan direktori dalam Keranjang Sampah untuk suatu drive:

`Clear-RecycleBin -DriveLetter {{C}}`

- Paksa hapus berkas dan direktori dalam Keranjang Sampah tanpa konfirmasi lebih lanjut:

`Clear-RecycleBin -Force`
