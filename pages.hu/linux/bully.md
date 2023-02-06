# bully

> A vezeték nélküli hozzáférési pont WPS-tűjének brutális kikényszerítése. A szükséges információkat a `airmon-ng` és a `airodump-ng` segítségével kell összegyűjteni a `bully` használata előtt. További információ: <https://salsa.debian.org/pkg-security-team/bully>.

- Törje fel a jelszót:

`bully --bssid "{{mac}}" --channel "{{channel}}" --bruteforce "{{interface}}"`

- Segítség megjelenítése:

`bully --help`
