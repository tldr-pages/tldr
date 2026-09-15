# GetHelpCmd OfficeActivationScenario

> Automatically repair activation-related issues within Microsoft Office / Microsoft 365 Apps for Enterprise.
> Part of `GetHelpCmd.exe`, formerly `SaRAcmd.exe` (Microsoft Support and Recovery Assistant).
> Note: This tool has been deprecated and will not work in the new OneNote and Outlook applications.
> Note: This command may override, deactivate, and/or remove your current volume of licensed Office product versions, so please proceed cautiously.
> See also: `ospp.vbs`.
> More information: <https://learn.microsoft.com/troubleshoot/microsoft-365/admin/miscellaneous/get-help-office-activation>.

- Automatically fix activation-related errors, close Office, and accept this command's End-User License Agreement (EULA). Requires Administrator privileges to do so:

`GetHelpCmd.exe -S OfficeActivationScenario -AcceptEula -CloseOffice`

- Detach the currently-installed Office licensing scheme from Shared Computer Activation (SCA), and activate the product separately. Requires Administrator privileges to do so:

`GetHelpCmd.exe -S OfficeActivationScenario -AcceptEula -CloseOffice -RemoveSCA`
