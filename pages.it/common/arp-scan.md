# arp-scan

> Invia pacchetti ARP agli host (IP o hostname) per scansionare la rete locale.
> Maggiori informazioni: <https://github.com/royhills/arp-scan>.

- Scansiona la rete locale corrente:

`arp-scan {{[-l|--localnet]}}`

- Scansiona un host specifico:

`arp-scan {{10.0.0.1}}`

- Scansiona una rete IP con maschera personalizzata:

`arp-scan {{192.168.1.1}}/{{24}}`

- Scansiona una rete IP in un intervallo personalizzato:

`arp-scan {{127.0.0.0}}-{{127.0.0.31}}`

- Scansiona una rete IP con maschera di sottorete personalizzata:

`arp-scan {{10.0.0.0}}:{{255.255.255.0}}`

- Specifica l'interfaccia di rete da usare per la scansione:

`arp-scan {{10.0.0.1}} {{[-I|--interface]}} {{nome_interfaccia}}`
