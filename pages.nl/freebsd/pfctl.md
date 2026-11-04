# pfctl

> Beheer het pakketfilterapparaat.
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?query=pfctl>.

- Schakel het pakketfilter in:

`sudo pfctl -e`

- Schakel het pakketfilter uit:

`sudo pfctl -d`

- Laad regels uit een configuratiebestand:

`sudo pfctl -f {{pad/naar/pf.conf}}`

- Toon alle actieve regels:

`pfctl -sr`

- Toon statusinformatie van het pakketfilter:

`pfctl -s info`

- Verwijder alle regels:

`sudo pfctl -F rules`
