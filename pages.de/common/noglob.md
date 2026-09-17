# noglob

> Führe Befehle in Zsh ohne Globbing aus (ohne Wildcard-Muster anzuwenden).
> Weitere Informationen: <https://manned.org/zshmisc>.

- Rufe eine URL ohne Anführungszeichen oder Escape-Sequenzen ab:

`noglob curl {{https://example.com?a=1}}`

- Öffne eine Datei, deren Name ein Sternchen enthält:

`noglob less {{*.txt}}`
