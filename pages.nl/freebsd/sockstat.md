# sockstat

> Toon open Internet- of UNIX-domeinsockets.
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?sockstat>.

- Bekijk welke gebruikers/processen [l]uisteren op welke poorten:

`sockstat -l`

- Toon informatie voor IPv[4]/IPv[6] sockets die [l]uisteren op specifieke [p]oorten met een specifiek [P]rotocol:

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{poort1,poort2...}}`

- Toon ook verbonden ([c]) sockets zonder [n]umerieke UID's om te zetten naar gebruikersnamen en met een [w]ijder veldformaat:

`sockstat -cnw`

- Toon alleen sockets die behoren tot een specifieke [j]ail ID of naam in [v]erbose modus:

`sockstat -jv`

- Toon de protocol[s]tatus en het externe [U]DP-encapsulatiepoortnummer, indien van toepassing (deze zijn momenteel alleen geïmplementeerd voor SCTP en TCP):

`sockstat -sU`

- Toon het [C]ongestiecontrolemodule en de protocol[S]tack, indien van toepassing (deze zijn momenteel alleen geïmplementeerd voor TCP):

`sockstat -CS`

- Toon alleen internetsockets als de lokale en buitenlandse adressen niet in het loopback-netwerkprefix 127.0.0.0/8 zitten, of niet het IPv6-loopbackadres ::1 bevatten:

`sockstat -L`

- Toon de koptekst niet ([q]uiet modus), toon [u]nix-sockets en geef de `inp_gencnt` weer:

`sockstat -qui`
