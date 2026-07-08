# lxc network

> Gestisce le reti per i container LXD.
> Maggiori informazioni: <https://documentation.ubuntu.com/lxd/latest/reference/manpages/lxc/network/>.

- Elenca tutte le reti disponibili:

`lxc network list`

- Mostra la configurazione di una rete specifica:

`lxc network show {{network_name}}`

- Aggiunge un'istanza in esecuzione a una rete specifica:

`lxc network attach {{network_name}} {{container_name}}`

- Crea una nuova rete gestita:

`lxc network create {{network_name}}`

- Imposta un'interfaccia bridge di una rete specifica:

`lxc network set {{network_name}} bridge.external_interfaces {{eth0}}`

- Disabilita NAT per una rete specifica:

`lxc network set {{network_name}} ipv{{4}}.nat false`
