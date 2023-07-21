# btrfs restore

> Tenta salvar arquivos de um sistema de arquivos btrfs danificado.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- Restaurar todos os arquivos de um sistema de arquivos btrfs para um determinado diretório:

`sudo btrfs restore {{caminho/para/dispositivo_btrfs}} {{caminho/para/diretório_alvo}}`

- Listar (sem escrever) os arquivos a serem restaurados de um sistema de arquivos btrfs:

`sudo btrfs restore --dry-run {{caminho/para/dispositivo_btrfs}} {{caminho/para/diretório_alvo}}`

- Restaurar arquivos correspondentes a determinados padrões regex ([c]ase-insensitive) de um sistema de arquivos btrfs (todos os diretórios pai do(s) arquivo(s) de destino também devem corresponder):

`sudo btrfs restore --path-regex {{regex}} -c {{caminho/para/dispositivo_btrfs}} {{caminho/para/diretório_alvo}}`

- Restaurar arquivos de um sistema de arquivos btrfs usando um `bytenr` específico da árvore raiz (consulte `btrfs-find-root`):

`sudo btrfs restore -t {{bytenr}} {{caminho/para/dispositivo_btrfs}} {{caminho/para/diretório_alvo}}`

- Restaurar arquivos de um sistema de arquivos btrfs (juntamente com metadados, atributos estendidos e Symlinks), sobrescrevendo arquivos no destino:

`sudo btrfs restore --metadata --xattr --symlinks --overwrite {{caminho/para/dispositivo_btrfs}} {{caminho/para/diretório_alvo}}`
