# Invoke-WebRequest

> HTTP/HTTPS-kérést hajt végre a weben. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Letölti egy URL-cím tartalmát egy fájlba:

`Invoke-WebRequest {{http://example.com}} -OutFile {{filename}}`

- Formulakódolt adatok küldése ( `application/x-www-form-urlencoded` típusú POST-kérelem):

`Invoke-WebRequest -Method Post -Body @{ name='bob' } {{http://example.com/form}}`

- Kérés küldése extra fejléccel, egyéni HTTP-módszerrel:

`Invoke-WebRequest -Headers {{@{ X-My-Header = '123' }}} -Method {{PUT}} {{http://example.com}}`

- Adatok küldése JSON formátumban, a megfelelő content-type fejléc megadásával:

`Invoke-WebRequest -Body {{'{"name":"bob"}'}} -ContentType 'application/json' {{http://example.com/users/1234}}`

- Felhasználónév és jelszó átadása a kiszolgáló hitelesítéséhez:

`Invoke-WebRequest -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("myusername:mypassword")) } {{http://example.com}}`
