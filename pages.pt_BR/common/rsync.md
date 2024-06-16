# rsync

> Transfira arquivos para ou de um host remote (mas não entre dois hosts remotos), usando SSH por padrão.
> Para especificar um caminho remoto, use `host:caminho/para/arquivo_ou_diretório`.
> Mais informações: <https://download.samba.org/pub/rsync/rsync.1>.

- Transfere um arquivo:

`rsync {{caminho/para/origem}} {{caminho/para/destino}}`

- Usa o modo de arquivo (copia recursivamente diretórios, copia links simbólicos sem resolver e preserva permissões, propriedade e tempos de modificação):

`rsync {{-a|--archive}} {{caminho/para/origem}} {{caminho/para/destino}}`

- Comprime os dados à medida que são enviados ao destino, exibe progresso detalhado e legível, e mantém arquivos parcialmente transferidos se forem interrompidos:

`rsync {{-zvhP|--compress --verbose --human-readable --partial --progress}} {{caminho/para/origem}} {{caminho/para/destino}}`

- Copia recursivamente diretórios:

`rsync {{-r|--recursive}} {{caminho/para/origem}} {{caminho/para/destino}}`

- Transfere os conteúdos do diretório, mas não o diretório em si:

`rsync {{-r|--recursive}} {{caminho/para/origem}}/ {{caminho/para/destino}}`

- Copia diretórios, usa o modo de arquivamento, resolve links simbólicos e ignora arquivos que são mais recentes no destino:

`rsync {{-auL|--archive --update --copy-links}} {{caminho/para/origem}} {{caminho/para/destino}}`

- Transfere um diretório para um host remoto executando o `rsyncd` and exclui arquivos no destino que não existem na origem:

`rsync {{-r|--recursive}} --delete rsync://{{host}}:{{caminho/para/origem}} {{caminho/para/destino}}`

- Transfere um arquivo por SSH usando uma porta diferente da padrão (22) e mostra o progresso global:

`rsync {{-e|--rsh}} 'ssh -p {{porta}}' --info=progress2 {{host}}:{{caminho/para/origem}} {{caminho/para/destino}}`
