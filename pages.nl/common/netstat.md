# netstat

> Toon netwerkgerelateerde informatie zoals open verbindingen, open socketpoorten, enz.
> Meer informatie: <https://manned.org/netstat>.

- Toon alle poorten:

`netstat {{[-a|--all]}}`

- Toon alle luisterende poorten:

`netstat {{-l|--listening]}}`

- Toon luisterende TCP-poorten:

`netstat {{-t|--tcp]}}`

- Toon PID en programmanamen:

`netstat {{[-p|--program]}}`

- Toon continu informatie:

`netstat {{[-c|--continuous]}}`

- Toon routes en los IP-adressen niet op naar hostnamen:

`netstat {{[-rn|--route --numeric]}}`

- Toon luisterende TCP- en UDP-poorten (+ gebruiker en proces als je root bent):

`netstat {{[-tulpne|--tcp --udp --listening --program --numeric --extend]}}`
