# Get-WUHistory

> Obtiene el historial de actualizaciones instaladas desde Windows Update. Parte del módulo externo `PSWindowsUpdate`.
> Este comando solo se puede ejecutar en PowerShell.
> Más información: <https://github.com/mgajda83/PSWindowsUpdate>.

- Obtiene la lista del historial de actualizaciones:

`Get-WUHistory`

- Lista las últimas 10 actualizaciones instaladas:

`Get-WUHistory -Last {{10}}`

- Lista todas las actualizaciones instaladas desde una fecha específica hasta hoy:

`Get-WUHistory -MaxDate {{fecha}}`

- Lista todas las actualizaciones instaladas en las últimas 24 horas:

`Get-WUHistory -MaxDate (Get-Date).AddDays(-1)`

- Envía los resultados por correo electrónico (SMTP):

`Get-WUHistory -SendReport -PSWUSettings @{SmtpServer="{{servidor_smtp}}"; Port={{puerto_smtp}} From="{{correo_remitente}}" To="{{correo_destinatario}}"}`
