# curl

> Perintah ini dapat merupakan alias dari `Invoke-WebRequest` jika program `curl` (<https://curl.se>) tidak terpasang secara benar di PowerShell.
> Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Cari tahu apakah `curl` sudah terpasang dengan benar dengan menampilkan versi program tersebut. Jika perintah ini memunculkan pesan galat/error, maka PowerShell berkemungkinan sedang menggantinya dengan `Invoke-WebRequest`:

`curl --version`

- Tampilkan dokumentasi untuk perintah `curl` yang asli:

`tldr curl -p common`

- Tampilkan dokumentasi untuk perintah `Invoke-WebRequest`:

`tldr invoke-webrequest`
