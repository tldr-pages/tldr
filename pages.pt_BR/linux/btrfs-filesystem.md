# btrfs filesystem

> Gerencia sistemas de arquivos btrfs.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- Mostra uso do sistema de arquivos (opcionalmente execute como root para mostrar informações detalhadas):

`btrfs filesystem usage {{caminho/para/montagem_btrfs}}`

- Mostra uso por dispositivos individuais:

`sudo btrfs filesystem show {{caminho/para/montagem_btrfs}}`

- Desfragmenta um único arquivo em um sistema de arquivos btrfs (evite enquanto um agente de desduplicação estiver em execução):

`sudo btrfs filesystem defragment -v {{caminho/para/arquivo}}`

- Desfragmenta um diretório recursivamente (não cruza os limites do subvolume):

`sudo btrfs filesystem defragment -v -r {{caminho/para/diretório}}`

- Força a sincronização de blocos de dados não gravados com o(s) disco(s):

`sudo btrfs filesystem sync {{caminho/para/montagem_btrfs}}`

- Resume o uso do disco para os arquivos em um diretório recursivamente:

`sudo btrfs filesystem du --summarize {{caminho/para/diretório}}`
