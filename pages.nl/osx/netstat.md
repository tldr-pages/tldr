# netstat

> Toon netwerkgerelateerde informatie zoals open verbindingen, open socketpoorten, enz.
> Zie ook: `lsof` voor het weergeven van netwerkverbindingen, inclusief luisterpoorten.
> Meer informatie: <https://keith.github.io/xcode-man-pages/netstat.1.html>.

- Toon de PID en programmanaam die luistert op een specifiek protocol:

`netstat -p {{protocol}}`

- Toon de routeringstabel en los IP-adressen niet op naar hostnamen:

`netstat -nr`

- Toon de routeringstabel van IPv4-adressen:

`netstat -nr -f inet`
