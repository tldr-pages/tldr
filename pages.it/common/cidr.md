# cidr

> Semplifica la gestione dei prefissi di rete IPv4/IPv6 CIDR con conteggio, controllo sovrapposizioni, spiegazioni e suddivisione.
> Maggiori informazioni: <https://github.com/bschaatsbergen/cidr>.

- Spiega un intervallo CIDR:

`cidr explain {{10.0.0.0/16}}`

- Controlla se un indirizzo appartiene a un intervallo CIDR:

`cidr contains {{10.0.0.0/16}} {{10.0.14.5}}`

- Conta tutti gli indirizzi in un intervallo CIDR:

`cidr count {{10.0.0.0/16}}`

- Controlla se due intervalli CIDR si sovrappongono:

`cidr overlaps {{10.0.0.0/16}} {{10.0.14.0/22}}`

- Suddividi un intervallo CIDR in un numero specifico di reti:

`cidr divide {{10.0.0.0/16}} {{9}}`
