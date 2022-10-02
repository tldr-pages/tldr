# snapper

> Ferramenta de gerenciamento de snapshots do sistema de arquivos.
> Mais informações: <http://snapper.io/manpages/snapper.html>.

- Lista configurações de snapshots:

`snapper list-configs`

- Criar configuração do snapper:

`snapper -c {{configuração}} create-config {{caminho/para/diretório}}`

- Criar um snapshot com uma descrição:

`snapper -c {{configuração}} create -d "{{descrição_do_snapshot}}"`

- Listar snapshots para uma configuração:

`snapper -c {{configuração}} list`

- Excluir um snapshot:

`snapper -c {{configuração}} delete {{número_do_snapshot}}`

- Excluir um intervalo de snapshots:

`snapper -c {{configuração}} delete {{snapshot_X}}-{{snapshot_Y}}`
