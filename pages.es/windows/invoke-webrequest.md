# Invoke-WebRequest

> Realiza una solicitud HTTP/HTTPS a la Web.
> Nota: Este comando solo se puede utilizar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Descarga el contenido de una URL a un archivo:

`Invoke-WebRequest {{http://example.com}} -OutFile {{ruta\al\archivo}}`

- Envía datos codificados para formularios (solicitud POST de tipo `application/x-www-form-urlencoded`):

`Invoke-WebRequest -Method Post -Body @{ name='roberto' } {{http://example.com/form}}`

- Envía una solicitud con un encabezado adicional, utilizando un método HTTP personalizado:

`Invoke-WebRequest -Headers {{@{ X-My-Header = '123' }}} -Method {{PUT}} {{http://example.com}}`

- Envía datos en formato JSON, especificando el encabezado tipo de contenido (content-type) adecuado:

`Invoke-WebRequest -Body {{'{"name":"bob"}'}} -ContentType 'application/json' {{http://example.com/users/1234}}`

- Pasa un nombre de usuario y contraseña para autenticación ante el servidor:

`Invoke-WebRequest -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("myusername:mypassword")) } {{http://example.com}}`
