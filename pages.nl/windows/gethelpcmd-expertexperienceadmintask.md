# GetHelpCmd ExpertExperienceAdminTask

> Verkrijg gedetailleerde installatie- en configuratie-informatie over verouderde Microsoft Outlook met Microsoft Office en Windows.
> Onderdeel van `GetHelpCmd.exe`, voorheen `SaRAcmd.exe` (Microsoft Support and Recovery Assistant).
> Opmerking: deze tool is verouderd en werkt niet in de nieuwe Outlook-applicatie.
> Meer informatie: <https://learn.microsoft.com/troubleshoot/microsoft-365/admin/miscellaneous/get-help-outlook-scan>.

- Verkrijg gedetailleerde informatie en accepteer de licentieovereenkomst voor eindgebruikers (EULA) van dit commando:

`GetHelpCmd.exe -S ExpertExperienceAdminTask -AcceptEula`

- Verkrijg gedetailleerde informatie en sla de logs op in een specifieke map:

`GetHelpCmd.exe -S ExpertExperienceAdminTask -AcceptEula -LogFolder {{pad\naar\map}}`

- Verkrijg gedetailleerde informatie zonder de voortgang te tonen:

`GetHelpCmd.exe -S ExpertExperienceAdminTask -AcceptEula -HideProgress`
