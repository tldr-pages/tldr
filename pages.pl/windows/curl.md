# curl

> W PowerShell to polecenie może być aliasem `Invoke-WebRequest`, gdy oryginalny program `curl` (<https://curl.se>) nie jest poprawnie zainstalowany.

- Zweryfikuj, czy `curl` jest poprawnie zainstalowany poprzez sprawdzenie jego wersji. Jeśli to polecenie zwraca błąd, PowerShell mógł je zastąpić poleceniem `Invoke-WebRequest`:

`curl --version`

- Zobacz dokumentację oryginalnego polecenia `curl`:

`tldr curl -p common`

- Zobacz dokumentację polecenia PowerShell `Invoke-WebRequest`:

`tldr invoke-webrequest`
