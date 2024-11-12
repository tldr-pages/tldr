# netstat

> Toon netwerkgerelateerde informatie zoals open verbindingen, open socketpoorten, enz.
> Meer informatie: <https://manned.org/netstat>.

- Toon alle poorten:

`netstat --all`

- Toon alle luisterende poorten:

`netstat --listening`

- Toon luisterende TCP-poorten:

`netstat --tcp`

- Toon PID en programmanamen:

`netstat --program`

- Toon informatie continu:

`netstat --continuous`

- Toon routes en los IP-adressen niet op naar hostnamen:

`netstat --route --numeric`

- Toon luisterende TCP- en UDP-poorten (+ gebruiker en proces als je root bent):

`netstat --listening --program --numeric --tcp --udp --extend`
