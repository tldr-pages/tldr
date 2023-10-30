# curl

> In PowerShell kan dit commando een alias zijn van `Invoke-WebRequest` als het originele `curl` programma (<https://curl.se>) niet correct is geïnstalleerd.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Controleer of `curl` correct is geïnstalleerd door het versienummer te printen. Als dit commando resulteert in een error, heeft PowerShell dit commando mogelijk vervangen met `Invoke-WebRequest`:

`curl --version`

- Bekijk de documentatie van het originele `curl` commando:

`tldr curl -p common`

- Bekijk de documentatie van het originele `curl` commando in een oudere versie van de `tldr` command-line client:

`tldr curl -o common`

- Bekijk de documentatie van het PowerShell's `Invoke-WebRequest` commando:

`tldr invoke-webrequest`
