# Invoke-WebRequest

> Membuat panggilan dan permintaan HTTP/HTTPS.
> Perintah ini hanya dapat digunakan dalam PowerShell.
> Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Unduh konten URL ke file:

`Invoke-WebRequest {{http://example.com}} -OutFile {{jalan/menuju/file}}`

- Mengirim data form yang telah di encode (permintaan POST atau tipe data `application/x-www-form-urlencoded`):

`Invoke-WebRequest -Method Post -Body @{ name='bob' } {{http://example.com/form}}`

- Mengirim sebuah permintaan dengan header tambahan, menggunakan metode HTTP kustom:

`Invoke-WebRequest -Headers {{@{ X-My-Header = '123' }}} -Method {{PUT}} {{http://example.com}}`

- Mengirim data dalam format JSON, Menentukan jenis konten yang sesuai header:

`Invoke-WebRequest -Body {{'{"name":"bob"}'}}  -ContentType 'application/json' {{http://example.com/users/1234}}`

- Memberikan nama pengguna dan kata sandi untuk otentikasi server:

`Invoke-WebRequest -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("myusername:mypassword")) } {{http://example.com}}`
