# btrfs property

> Obtém, define ou lista propriedades para um determinado objeto de sistema de arquivos btrfs (arquivos, diretórios, subvolumes, sistemas de arquivos ou dispositivos).
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-property.html>.

- Lista as propriedades disponíveis (e descrições) para o objeto btrfs fornecido:

`sudo btrfs property list {{caminho/para/objeto_btrfs}}`

- Obtém todas as propriedades para o objeto btrfs fornecido:

`sudo btrfs property get {{caminho/para/objeto_btrfs}}`

- Obtém a propriedade `label` (etiqueta) para o sistema de arquivos ou dispositivo btrfs fornecido:

`sudo btrfs property get {{caminho/para/sistema_de_arquivos_btrfs}} label`

- Obtém todas as propriedades específicas do tipo de objeto para o sistema de arquivos ou dispositivo btrfs fornecido:

`sudo btrfs property get -t {{subvol|filesystem|inode|device}} {{caminho/para/sistema_de_arquivos_btrfs}}`

- Define a propriedade de `compression` (compactação) para um determinado inode btrfs (um arquivo ou diretório):

`sudo btrfs property set {{caminho/para/inode_btrfs}} compression {{zstd|zlib|lzo|none}}`
