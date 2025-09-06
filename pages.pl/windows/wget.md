# wget

> W PowerShell to polecenie może być aliasem `Invoke-WebRequest`, gdy oryginalny program `wget` (<https://www.gnu.org/software/wget>) nie jest poprawnie zainstalowany.
> Więcej informacji: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Zobacz dokumentację oryginalnego polecenia `wget`:

`tldr wget -p common`

- Zobacz dokumentację polecenia PowerShell `Invoke-WebRequest`:

`tldr invoke-webrequest`

- Zweryfikuj, czy `wget` jest poprawnie zainstalowany poprzez sprawdzenie jego wersji. Jeśli to polecenie zwraca błąd, PowerShell mógł je zastąpić poleceniem `Invoke-WebRequest`:

`wget --version`
