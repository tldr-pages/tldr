# bup

> Sistema de backup baseado no formato Git packfile, oferecendo salvamentos incrementais e desduplicação global.
> Mais informações: <https://manned.org/bup>.

- Inicializa um repositório de backup no diretório local especificado:

`bup {{[-d|--bup-dir]}} {{caminho/para/repositório}} init`

- Prepara um determinado diretório antes de fazer um backup:

`bup {{[-d|--bup-dir]}} {{caminho/para/repositório}} index {{caminho/para/diretório}}`

- Faz o backup de um diretório para o repositório:

`bup {{[-d|--bup-dir]}} {{caminho/para/repositório}} save {{[-n|--name]}} {{nome_do_backup}} {{caminho/para/diretório}}`

- Exibe os snapshots de backup armazenados atualmente no repositório:

`bup {{[-d|--bup-dir]}} {{caminho/para/repositório}} ls`

- Restaura um snapshot de backup específico para um diretório de destino:

`bup {{[-d|--bup-dir]}} {{caminho/para/repositório}} restore {{[-C|--outdir]}} {{caminho/para/diretório_de_destino}} {{nome_do_backup}}`
