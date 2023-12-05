# ipconfig

> Zeigt die Netzwerkkonfiguration von Windows an und verwaltet diese.
> Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Zeigt eine Liste der Netzwerkadapter an:

`ipconfig`

- Zeigt eine detaillierte Liste der Netzwerkadapter an:

`ipconfig /all`

- Erneuert die IP-Adressen für einen Netzwerk Adapter:

`ipconfig /renew {{Adapter}}`

- Gibt die IP-Adressen für einen Netzwerkadapter frei:

`ipconfig /release {{Adapter}}`

- Zeigt den lokalen DNS-Cache an:

`ipconfig /displaydns`

- Entfernt alle Daten aus dem lokalen DNS-Cache:

`ipconfig /flushdns`
