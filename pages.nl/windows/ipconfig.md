# ipconfig

> Toon en beheer de netwerkconfiguratie van Windows.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Toon alle netwerkadapters:

`ipconfig`

- Toon een gedetailleerde lijst van netwerkadapters:

`ipconfig /all`

- Vernieuw de IP-adressen voor een netwerkadapter:

`ipconfig /renew {{adapter}}`

- Laat de IP-adressen voor een netwerkadapter vrij:

`ipconfig /release {{adapter}}`

- Toon de lokale DNS-cache:

`ipconfig /displaydns`

- Verwijder alle gegevens uit de lokale DNS-cache:

`ipconfig /flushdns`
