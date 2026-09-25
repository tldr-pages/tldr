# GetHelpCmd OutlookCalendarCheckTask

> Busca problemas de configuración del calendario en aplicaciones heredadas de Microsoft Outlook.
> Forma parte de `GetHelpCmd.exe`, anteriormente `SaRAcmd.exe` (Asistente de soporte y recuperación de Microsoft).
> Nota: Esta herramienta ha quedado obsoleta y no funcionará en la nueva aplicación de Outlook.
> Más información: <https://learn.microsoft.com/troubleshoot/microsoft-365/admin/miscellaneous/get-help-outlook-calendar-scan>.

- Analiza el calendario del perfil activo actual y acepta el Acuerdo de licencia de usuario final (EULA) de este comando:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula`

- Analiza el calendario de un perfil específico de Outlook:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula -P {{perfil}}`

- Analiza el calendario de un perfil específico y guarda los registros en un directorio concreto:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula -P {{profile}} -LogFolder {{ruta\al\directorio}}`

- Analiza el calendario de un perfil específico sin mostrar el progreso:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula -P {{perfil}} -HideProgress`
