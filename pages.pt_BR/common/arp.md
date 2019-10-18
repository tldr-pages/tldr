# arp

> Mostrar e manipular a cache ARP do sistema.

- Mostrar a tabela arp atual:

`arp -a`

- Limpar toda a cache:

`sudo arp -a -d`

- Eliminar uma entrada específica:

`arp -d {{endereço}}`

- Criar uma entrada:

`arp -s {{endereço}} {{endereço_mac}}`
