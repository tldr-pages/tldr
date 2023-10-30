# wget

> Perintah ini dapat merupakan alias dari `Invoke-WebRequest` jika program `wget` (<https://www.gnu.org/software/wget>) tidak terpasang secara benar di PowerShell.
> Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Cari tahu apakah `wget` sudah terpasang dengan benar dengan menampilkan versi program tersebut. Jika perintah ini memunculkan pesan galat/error, maka PowerShell berkemungkinan sedang menggantinya dengan `Invoke-WebRequest`:

`curl --version`

- Tampilkan dokumentasi untuk perintah `wget` yang asli:

`tldr wget -p common`

- Tampilkan dokumentasi untuk perintah `wget` yang asli dalam program `tldr` versi lawas:

`tldr wget -o common`

- Tampilkan dokumentasi untuk perintah `Invoke-WebRequest`:

`tldr invoke-webrequest`
