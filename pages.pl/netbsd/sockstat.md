# sockstat

> Wyświetl listę otwartych gniazd internetowych lub UNIX-owych.
> Uwaga: ten program jest przeróbką programu `sockstat` z FreeBSD dla NetBSD 3.0.
> Zobacz także: `netstat`.
> Więcej informacji: <https://man.netbsd.org/sockstat.1>.

- Pokaż informacje o gniazdach IPv4, IPv6 i Unix, zarówno nasłuchujących jak i połączonych:

`sockstat`

- Pokaż informacje o gniazdach IPv[4]/IPv[6] nasłuchujących (z ang. [l]istening) na określonych [p]ortach używając określonego [P]rotokołu:

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{port1,port2...}}`

- Pokaż również połączone (z ang. [c]onnected) gniazda, wyświetlając gniazda [u]nixowe:

`sockstat -cu`

- Pokaż tylko wynik [n]umeryczny, bez rozwiązywania symbolicznych nazw dla adresów i portów:

`sockstat -n`

- Pokaż tylko gniazda dla określonej rodziny (z ang. [f]amily) adresów:

`sockstat -f {{inet|inet6|local|unix}}`
