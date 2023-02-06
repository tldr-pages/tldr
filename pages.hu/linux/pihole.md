# pihole

> A Pi-hole hirdetésblokkoló DNS-kiszolgáló terminálfelülete. További információ: <https://docs.pi-hole.net/core/pihole-command/>.

- Ellenőrizze a Pi-hole démon állapotát:

`pihole status`

- Pi-hole és a Gravity frissítése:

`pihole -up`

- A rendszer részletes állapotának figyelése:

`pihole chronometer`

- A démon indítása vagy leállítása:

`pihole {{enable|disable}}`

- A démon (nem maga a kiszolgáló) újraindítása:

`pihole restartdns`

- Egy tartomány fehér vagy fekete listára kerülése:

`pihole {{whitelist|blacklist}} {{example.com}}`

- Keresés a listákon egy tartományra vonatkozóan:

`pihole query {{example.com}}`

- A kapcsolatok valós idejű naplójának megnyitása:

`pihole tail`
