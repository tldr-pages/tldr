# ip link

> Gestionați interfețele de rețea.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/ip-link.8.html>

- Afișați informații despre toate interfețele de rețea:

`ip link`

- Afișați informații despre o anumită interfață de rețea:

`ip link show {{ethN}}`

- Adu o interfață de rețea în sus sau în jos:

`ip link set {{ethN}} {{up|down}}`

- Dați un nume semnificativ unei interfețe de rețea:

`ip link set {{ethN}} alias "{{LAN Interface}}"`

- Schimbarea adresei MAC a unei interfețe de rețea:

`ip link set {{ethN}} address {{ff:ff:ff:ff:ff:ff}}`

- Modificați dimensiunea MTU pentru o interfață de rețea pentru a utiliza cadre jumbo:

`ip link set {{ethN}} mtu {{9000}}`
