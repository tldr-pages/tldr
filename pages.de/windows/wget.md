# wget

> In PowerShell kann dieser Befehl ein Alias von `Invoke-WebRequest` sein, wenn das Originalprogramm `wget` (<https://www.gnu.org/software/wget>) nicht ordnungsgemäß installiert wurde.
> Weitere Informationen: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Schaue dir hier die Dokumentation für den ursprünglichen `wget`-Befehl an:

`tldr wget -p common`

- Schaue dir hier die Dokumentation für den PowerShell-Befehl `Invoke-WebRequest` an:

`tldr invoke-webrequest`

- Überprüfen Sie, ob `wget` ordnungsgemäß installiert ist, indem Sie sich die Versionsnummer ausgeben lassen. Wenn nachfolgender Befehl einen Fehler ausgibt, hat PowerShell diesen Befehl möglicherweise durch `Invoke-WebRequest` ersetzt:

`wget --version`
