# btrfs rescue

> Tenta recuperar um sistema de arquivos btrfs danificado.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

- Reconstrói a árvore de metadados do sistema de arquivos (muito lento):

`sudo btrfs rescue chunk-recover {{caminho/para/partição}}`

- Corrige problemas relacionados ao alinhamento do tamanho do dispositivo (por exemplo, incapaz de montar o sistema de arquivos com incompatibilidade de super total de bytes):

`sudo btrfs rescue fix-device-size {{caminho/para/partição}}`

- Recupera um superblock corrompido das cópias corretas (recupere a raiz da árvore do sistema de arquivos):

`sudo btrfs rescue super-recover {{caminho/para/partição}}`

- Recupera-se de uma transação interrompida (corrige problemas de repetição de log):

`sudo btrfs rescue zero-log {{caminho/para/partição}}`

- Cria um dispositivo de controle `/dev/btrfs-control` quando o `mknod` não estiver instalado:

`sudo btrfs rescue create-control-device`
