# GetHelpCmd OutlookCalendarCheckTask

> Scan op agendaconfiguratieproblemen in verouderde Microsoft Outlook-applicaties.
> Onderdeel van `GetHelpCmd.exe`, voorheen `SaRAcmd.exe` (Microsoft Support and Recovery Assistant).
> Opmerking: deze tool is verouderd en werkt niet in de nieuwe Outlook-applicatie.
> Meer informatie: <https://learn.microsoft.com/troubleshoot/microsoft-365/admin/miscellaneous/get-help-outlook-calendar-scan>.

- Analyseer de agenda voor het huidige, actieve profiel, en accepteer de licentieovereenkomst voor eindgebruikers (EULA) van dit commando:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula`

- Analyseer de agenda voor een specifiek Outlook-profiel:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula -P {{profiel}}`

- Analyseer de agenda voor een specifiek profiel en sla de logs op in een specifieke map:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula -P {{profiel}} -LogFolder {{pad\naar\map}}`

- Analyseer de agenda voor een specifiek profiel zonder de voortgang te tonen:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula -P {{profiel}} -HideProgress`
