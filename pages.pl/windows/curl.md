# curl

> W PowerShell polecenie to może być aliasem polecenia `Invoke-WebRequest`, gdy oryginalny program `curl` (<https://curl.se>) nie jest poprawnie zainstalowany.

- Zweryfikuj, czy `curl` jest poprawnie zainstalowany przez sprawdzeniem jego wersji. Jeśli to polecenie zwraca błąd, PowerShell mógł zastąpić to polecenie `Invoke-WebRequest`:

`curl --version`

- Zobacz dokumentację orginalnego polecenia `curl`:

`tldr curl -p common`

- Zobacz dokumentację polecenia PowerShell `Invoke-WebRequest`:

`tldr invoke-webrequest`
