# arp-scan

> Trimiteți pachete ARP către gazde (specificate ca adrese IP sau nume de gazdă) pentru a scana rețeaua locală.
> Mai multe informaţii: <https://github.com/royhills/arp-scan>

- Scanați rețeaua locală curentă:

`arp-scan --localnet`

- Scanarea unei rețele IP cu o mască de bitmask personalizată:

`arp-scan {{192.168.1.1}}/{{24}}`

- Scanarea unei rețele IP într-un interval personalizat:

`arp-scan {{127.0.0.0}}-{{127.0.0.31}}`

- Scanarea unei rețele IP cu o mască netă personalizată:

`arp-scan {{10.0.0.0}}:{{255.255.255.0}}`
