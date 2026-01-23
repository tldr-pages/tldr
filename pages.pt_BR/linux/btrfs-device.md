# btrfs device

> Gerencia dispositivos em um sistema de arquivos btrfs.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- Adiciona um ou mais dispositivos a um sistema de arquivos btrfs:

`sudo btrfs {{[d|device]}} {{[a|add]}} {{caminho/para/bloco_do_dispositivo1 caminho/para/bloco_do_dispositivo2 ...}} {{caminho/para/sistema_de_arquivos_btrfs}}`

- Remove um dispositivo de um sistema de arquivos btrfs:

`sudo btrfs {{[d|device]}} {{[rem|remove]}} {{caminho/para/dispositivo|id_do_dispositivo}} [{{...}}]`

- Exibe estatísticas de erro:

`sudo btrfs {{[d|device]}} {{[st|stats]}} {{caminho/para/sistema_de_arquivos_btrfs}}`

- Examina todos os discos e informa ao kernel todos os sistemas de arquivos btrfs detectados:

`sudo btrfs {{[d|device]}} {{[sc|scan]}} {{[-d|--all-devices]}}`

- Exibe estatísticas detalhadas de alocação por disco:

`sudo btrfs {{[d|device]}} {{[u|usage]}} {{caminho/para/sistema_de_arquivos_btrfs}}`
