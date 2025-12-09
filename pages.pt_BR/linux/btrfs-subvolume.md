# btrfs subvolume

> Gerencia subvolumes e snapshots btrfs.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- Cria um novo subvolume vazio:

`sudo btrfs subvolume create {{caminho/para/novo_subvolume}}`

- Lista todos os subvolumes e snapshots no sistema de arquivos especificado:

`sudo btrfs subvolume list {{caminho/para/sistema_de_arquivos_btrfs}}`

- Exclui um subvolume:

`sudo btrfs subvolume delete {{caminho/para/subvolume}}`

- Cria um snapshot somente leitura de um subvolume existente:

`sudo btrfs subvolume snapshot -r {{caminho/para/subvolume_de_origem}} {{caminho/para/destino}}`

- Cria um snapshot de leitura/gravação de um subvolume existente:

`sudo btrfs subvolume snapshot {{caminho/para/subvolume_de_origem}} {{caminho/para/destino}}`

- Mostra informações detalhadas sobre um subvolume:

`sudo btrfs subvolume show {{caminho/para/subvolume}}`
