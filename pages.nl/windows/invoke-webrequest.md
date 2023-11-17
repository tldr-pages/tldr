# Invoke-WebRequest

> Voer een HTTP/HTTPS request uit naar het Web.
> Dit commando kan alleen gebruikt worden via PowerShell.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Download de inhoud van een URL naar een bestand:

`Invoke-WebRequest {{http://example.com}} -OutFile {{pad\naar\bestand}}`

- Stuur form-gecodeerde gegevens (POST request van het type `application/x-www-form-urlencoded`):

`Invoke-WebRequest -Method Post -Body @{ name='bob' } {{http://example.com/form}}`

- Stuur een request met een extra header, door gebruik te maken van een aangepast HTTP methode:

`Invoke-WebRequest -Headers {{@{ X-My-Header = '123' }}} -Method {{PUT}} {{http://example.com}}`

- Stuur gegevens in JSON formaat en specificieer de juiste content-type header:

`Invoke-WebRequest -Body {{'{"name":"bob"}'}} -ContentType 'application/json' {{http://example.com/users/1234}}`

- Stuur een gebruikersnaam en wachtwoord voor een server authenticatie:

`Invoke-WebRequest -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("myusername:mypassword")) } {{http://example.com}}`
