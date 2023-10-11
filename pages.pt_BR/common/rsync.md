# rsync

> Transfira arquivos para ou de um host remote (mas não entre dois hosts remotos), usando SSH por padrão.
> para especificar um caminho remoto, use `host:caminho/para/arquivo_ou_diretório`.
> Mais informações: <https://download.samba.org/pub/rsync/rsync.1>.

- Transferir um arquivo:

`rsync {{caminho/para/origem}} {{caminho/para/destino}}`

- Usar o modo de arquivo (recursivamente copiar diretórios, copiar links simbólicos sem resolver e preservar permissões, propriedade e tempos de modificação):

`rsync --archive {{caminho/para/origem}} {{caminho/para/destino}}`

- Comprimir os dados à medida que são enviados ao destino, exibir progresso detalhado e legível, e manter arquivos parcialmente transferidos se forem interrompidos:

`rsync --compress --verbose --human-readable --partial --progress {{caminho/para/origem}} {{caminho/para/destino}}`

- Recursivamente copiar diretórios:

`rsync --recursive {{caminho/para/origem}} {{caminho/para/destino}}`

- Transferir os conteúdos do diretório, mas não o diretório em si:

`rsync --recursive {{caminho/para/origem}}/ {{caminho/para/destino}}`

- Recursivamente copiar diretórios, user modo de arquivo, resolver links simbólicos e ignorar arquivos que são mais recentes no destino:

`rsync --recursive --archive --update --copy-links {{caminho/para/origem}} {{caminho/para/destino}}`

- Transferir um diretório para um host remoto executando o `rsyncd` and excluir arquivos no destino que não existam na origem:

`rsync --recursive --delete rsync://{{host}}:{{caminho/para/origem}} {{caminho/para/destino}}`

- Transferir um arquivo por SSH usando uma porta diferente da padrão (22) e mostrar o progresso global:

`rsync --rsh 'ssh -p {{porta}}' --info=progress2 {{host}}:{{caminho/para/origem}} {{caminho/para/destino}}`
