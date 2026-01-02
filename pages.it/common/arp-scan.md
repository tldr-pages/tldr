# arp-scan

> Invia pacchetti ARP agli host (specificati come indirizzi IP o nomi host) per scansionare la rete locale.
> Maggiori informazioni: <https://github.com/royhills/arp-scan>.

- Scansiona la rete locale corrente:

`arp-scan {{[-l|--localnet]}}`

- Scansiona una rete IP con una maschera di bit personalizzata:

`arp-scan {{192.168.1.1}}/{{24}}`

- Scansiona una rete IP all'interno di un intervallo personalizzato:

`arp-scan {{127.0.0.0}}-{{127.0.0.31}}`

- Scansiona una rete IP con una maschera di rete personalizzata:

`arp-scan {{10.0.0.0}}:{{255.255.255.0}}`
