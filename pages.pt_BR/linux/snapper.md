# snapper

> Ferramenta de gerenciamento de snapshots do sistema de arquivos.
> Mais informações: <http://snapper.io/manpages/snapper.html>.

- Lista configurações de snapshots:

`snapper list-configs`

- Cria configuração do snapper:

`snapper {{[-c|--config]}} {{configuração}} create-config {{caminho/para/diretório}}`

- Cria um snapshot com uma descrição:

`snapper {{[-c|--config]}} {{configuração}} create {{[-d|--description]}} "{{descrição_do_snapshot}}"`

- Lista snapshots para uma configuração:

`snapper {{[-c|--config]}} {{configuração}} list`

- Exclue um snapshot:

`snapper {{[-c|--config]}} {{configuração}} delete {{número_do_snapshot}}`

- Exclue um intervalo de snapshots:

`snapper {{[-c|--config]}} {{configuração}} delete {{snapshot_X}}-{{snapshot_Y}}`
