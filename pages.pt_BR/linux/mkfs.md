# mkfs

> Cria um sistema de arquivos Linux em uma partição do disco rígido.
> Esse comando está obsoleto em favor dos utilitários mkfs.<tipo> específicos de sistema de arquivos.
> Mais informações: <https://manned.org/mkfs>.

- Cria um sistema de arquivo ext2 do Linux em uma partição:

`sudo mkfs {{caminho/para/partição}}`

- Cria um sistema de arquivos de um tipo especificado:

`sudo mkfs {{[-t|--type]}} {{ext4}} {{caminho/para/partição}}`

- Cria um sistema de arquivos de um tipo especificado e verifica por blocos ruins:

`sudo mkfs -c {{[-t|--type]}} {{ntfs}} {{caminho/para/partição}}`
