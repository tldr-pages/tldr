# snoop

> Network packet sniffer. A tcpdump SunOS megfelelője. További információ: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Csomagok rögzítése egy adott hálózati interfészen:

`snoop -d {{e1000g0}}`

- A rögzített csomagok mentése egy fájlba a megjelenítés helyett:

`snoop -o {{filename}}`

- A csomagok verbózus protokollréteg-összefoglalójának megjelenítése egy fájlból:

`snoop -V -i {{filename}}`

- Egy hostnévről érkező és egy adott portra érkező hálózati csomagok rögzítése:

`snoop to port {{port}} from host {{hostname}}`

- A két IP-cím között kicserélt hálózati csomagok hex-dumpjának rögzítése és megjelenítése:

`snoop -x0 -p4 {{ip_address_1}} {{ip_address_2}}`
