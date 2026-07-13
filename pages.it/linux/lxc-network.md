# lxc network

> Gestisce le reti per i container LXD.
> Maggiori informazioni: <https://documentation.ubuntu.com/lxd/latest/reference/manpages/lxc/network/>.

- Elenca tutte le reti disponibili:

`lxc network list`

- Mostra la configurazione di una rete specifica:

`lxc network show {{nome_network}}`

- Aggiunge un'istanza in esecuzione a una rete specifica:

`lxc network attach {{nome_network}} {{nome_container}}`

- Crea una nuova rete gestita:

`lxc network create {{nome_network}}`

- Imposta un'interfaccia bridge di una rete specifica:

`lxc network set {{nome_network}} bridge.external_interfaces {{eth0}}`

- Disabilita NAT per una rete specifica:

`lxc network set {{nome_network}} ipv{{4}}.nat false`
