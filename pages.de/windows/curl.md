# curl

> In PowerShell kann dieser Befehl ein Alias von `Invoke-WebRequest` sein, wenn das Originalprogramm `curl` (<https://curl.se>) nicht ordnungsgemäß installiert wurde.
> Weitere Informationen: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Überprüfen Sie, ob `curl` ordnungsgemäß installiert ist, indem Sie sich die Versionsnummer ausgeben lassen. Wenn nachfolgender Befehl einen Fehler ausgibt, hat PowerShell diesen Befehl möglicherweise durch `Invoke-WebRequest` ersetzt:

`curl --version`

- Schaue dir hier die Dokumentation für den ursprünglichen `curl`-Befehl an:

`tldr curl -p common`

- Schaue dir hier die Dokumentation für den PowerShell-Befehl `Invoke-WebRequest` an:

`tldr invoke-webrequest`
