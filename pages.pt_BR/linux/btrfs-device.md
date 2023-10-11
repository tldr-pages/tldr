# btrfs device

> Gerencia dispositivos em um sistema de arquivos btrfs.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- Adiciona um ou mais dispositivos a um sistema de arquivos btrfs:

`sudo btrfs device add {{caminho/para/bloco_do_dispositivo1}} [{{caminho/para/bloco_do_dispositivo2}}] {{caminho/para/sistema_de_arquivos_btrfs}}`

- Remove um dispositivo de um sistema de arquivos btrfs:

`sudo btrfs device remove {{caminho/para/dispositivo|id_do_dispositivo}} [{{...}}]`

- Exibe estatísticas de erro:

`sudo btrfs device stats {{caminho/para/sistema_de_arquivos_btrfs}}`

- Examina todos os discos e informa ao kernel todos os sistemas de arquivos btrfs detectados:

`sudo btrfs device scan --all-devices`

- Exibe estatísticas detalhadas de alocação por disco:

`sudo btrfs device usage {{caminho/para/sistema_de_arquivos_btrfs}}`
