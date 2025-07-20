# Get-WUApiVersion

> Obtiene la versión del Agente de Windows Update. Parte del módulo externo `PSWindowsUpdate`.
> Este comando solo se puede ejecutar en PowerShell.
> Más información: <https://github.com/mgajda83/PSWindowsUpdate>.

- Obtiene la versión actualmente instalada del Agente de Windows Update:

`Get-WUApiVersion`

- Envía los datos de configuración actuales por correo electrónico (SMTP):

`Get-WUApiVersion -SendReport -PSWUSettings @{SmtpServer="{{servidor_smtp}}"; Port={{puerto_smtp}} From="{{correo_remitente}}" To="{{correo_destinatario}}"}`
