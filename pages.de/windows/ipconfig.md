# ipconfig

> Zeige die Netzwerkkonfiguration von Windows an und verwalte diese.
> Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Zeige eine Liste der Netzwerkadapter an:

`ipconfig`

- Zeige eine detaillierte Liste der Netzwerkadapter an:

`ipconfig /all`

- Erneuere die IP-Adressen für einen Netzwerkadapter:

`ipconfig /renew {{Adapter}}`

- Gib die IP-Adressen für einen Netzwerkadapter frei:

`ipconfig /release {{Adapter}}`

- Zeige den lokalen DNS-Cache an:

`ipconfig /displaydns`

- Entferne alle Einträge aus dem lokalen DNS-Cache:

`ipconfig /flushdns`
