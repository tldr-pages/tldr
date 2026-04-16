# GetHelpCmd OutlookCalendarCheckTask

> Scan for calendar configuration issues in legacy Microsoft Outlook applications.
> Part of `GetHelpCmd.exe`, formerly `SaRAcmd.exe` (Microsoft Support and Recovery Assistant).
> Note: This tool has been deprecated and will not work in the new Outlook application.
> More information: <https://learn.microsoft.com/troubleshoot/microsoft-365/admin/miscellaneous/get-help-outlook-calendar-scan>.

- Analyse the calendar for the current, active profile, and accept this command's End-User License Agreement (EULA):

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula`

- Analyse calendar for a specific Outlook profile:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula -P {{profile}}`

- Analyze the calendar for a specific profile and save the logs to a specific directory:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula -P {{profile}} -LogFolder {{path\to\file}}`

- Analyse calendar for a specific profile and hide the program progress:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula -P {{profile}} -HideProgress`
