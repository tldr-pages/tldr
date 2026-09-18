# ip netconf

> Mostra i parametri di configurazione.
> Maggiori informazioni: <https://manned.org/ip-netconf>.

- Mostra la configurazione di rete per tutte le interfacce:

`ip {{[netc|netconf]}}`

- Mostra la configurazione di rete per un'interfaccia specifica:

`ip {{[netc|netconf]}} {{[s|show]}} dev {{network_interface}}`

- Mostra solo la configurazione di rete IPv4:

`ip -4 {{[netc|netconf]}}`

- Mostra solo la configurazione di rete IPv6:

`ip -6 {{[netc|netconf]}}`
