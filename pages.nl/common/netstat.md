# netstat

> Toon netwerkgerelateerde informatie zoals open verbindingen, open socketpoorten, enz.
> Meer informatie: <https://manned.org/netstat>.

- Lijst alle poorten:

`netstat --all`

- Lijst alle luisterende poorten:

`netstat --listening`

- Lijst luisterende TCP-poorten:

`netstat --tcp`

- Toon PID en programmanamen:

`netstat --program`

- Lijst informatie continu:

`netstat --continuous`

- Lijst routes en los IP-adressen niet op naar hostnamen:

`netstat --route --numeric`

- Lijst luisterende TCP- en UDP-poorten (+ gebruiker en proces als je root bent):

`netstat --listening --program --numeric --tcp --udp --extend`
