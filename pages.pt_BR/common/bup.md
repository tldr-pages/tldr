# bup

> Sistema de backup baseado no formato Git packfile, oferecendo salvamentos incrementais e desduplicação global.
> Mais informações: <https://github.com/bup/bup>.

- Inicializa um repositório de backup no diretório local especificado:

`bup -d {{caminho/para/repositório}} init`

- Prepara um determinado diretório antes de fazer um backup:

`bup -d {{caminho/para/repositório}} index {{caminho/para/diretório}}`

- Faz o backup de um diretório para o repositório:

`bup -d {{caminho/para/repositório}} save -n {{nome_do_backup}} {{caminho/para/diretório}}`

- Exibe os snapshots de backup armazenados atualmente no repositório:

`bup -d {{caminho/para/repositório}} ls`

- Restaura um snapshot de backup específico para um diretório de destino:

`bup -d {{caminho/para/repositório}} restore -C {{caminho/para/diretório_de_destino}} {{nome_do_backup}}`
