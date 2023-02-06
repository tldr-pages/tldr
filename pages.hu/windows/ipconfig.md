# ipconfig

> A Windows hálózati konfigurációjának megjelenítése és kezelése. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- A hálózati adapterek listájának megjelenítése:

`ipconfig`

- A hálózati adapterek részletes listájának megjelenítése:

`ipconfig /all`

- A hálózati adapter IP-címeinek megújítása:

`ipconfig /renew {{adapter}}`

- Egy hálózati adapter IP-címeinek felszabadítása:

`ipconfig /release {{adapter}}`

- Minden adat eltávolítása a DNS gyorsítótárból:

`ipconfig /flushdns`
