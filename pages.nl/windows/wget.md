# wget

> In PowerShell kan dit commando een alias zijn van `Invoke-WebRequest` als het originele `wget` programma (<https://www.gnu.org/software/wget>) niet correct is geïnstalleerd.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Controleer of `wget` correct is geïnstalleerd door het versienummer te printen. Als dit commando resulteert in een error, heeft PowerShell dit commando mogelijk vervangen met `Invoke-WebRequest`:

`wget --version`

- Bekijk de documentatie van het originele `wget` commando:

`tldr wget -p common`

- Bekijk de documentatie van het PowerShell's `Invoke-WebRequest` commando:

`tldr invoke-webrequest`
