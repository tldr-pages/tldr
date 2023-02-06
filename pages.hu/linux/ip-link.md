# ip link

> Hálózati interfészek kezelése. További információ: <https://man7.org/linux/man-pages/man8/ip-link.8.html>.

- Az összes hálózati interfészre vonatkozó információk megjelenítése:

`ip link`

- Egy adott hálózati interfészre vonatkozó információk megjelenítése:

`ip link show {{ethN}}`

- Hálózati interfész fel- vagy leállítása:

`ip link set {{ethN}} {{up|down}}`

- Értelmes nevet adhat egy hálózati interfésznek:

`ip link set {{ethN}} alias "{{LAN Interface}}"`

- A hálózati interfész MAC-címének módosítása:

`ip link set {{ethN}} address {{ff:ff:ff:ff:ff:ff}}`

- A hálózati interfész MTU méretének módosítása a jumbo-keretek használatához:

`ip link set {{ethN}} mtu {{9000}}`
