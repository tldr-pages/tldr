# rclone

> Copia, sincroniza ou move arquivos e diretórios de e para diversos serviços em nuvem.
> Mais informações: <https://rclone.org/commands/rclone/>.

- Inicia um menu interativo para configurar o rclone:

`rclone config`

- Lista o conteúdo de um diretório em um armazenamento remoto do rclone:

`rclone lsf {{nome_do_remoto}}:{{caminho/para/diretorio}}`

- Copia um arquivo ou diretório da máquina local para o destino remoto:

`rclone copy {{caminho/para/arquivo_ou_diretorio_origem}} {{nome_do_remoto}}:{{caminho/para/diretorio}}`

- Copia arquivos alterados nas últimas 24 horas da máquina local para um remoto, solicitando confirmação para cada arquivo:

`rclone copy {{[-i|--interactive]}} --max-age 24h {{nome_do_remoto}}:{{caminho/para/diretorio}} {{caminho/para/diretorio_local}}`

- Espelha um arquivo ou diretório específico (Nota: Ao contrário de copy, sync remove arquivos do remoto se eles não existirem localmente):

`rclone sync {{caminho/para/arquivo_ou_diretorio}} {{nome_do_remoto}}:{{caminho/para/diretorio}}`

- Simula a exclusão de um arquivo ou diretório remoto (remova `--dry-run` do comando para realmente excluir):

`rclone {{[-n|--dry-run]}} delete {{nome_do_remoto}}:{{caminho/para/arquivo_ou_diretorio}}`

- Monta um armazenamento remoto do rclone (experimental):

`rclone mount {{nome_do_remoto}}:{{caminho/para/diretorio}} {{caminho/para/ponto_de_montagem}}`

- Desmonta um armazenamento remoto do rclone se `<Ctrl c>` falhar (experimental):

`fusermount {{[-u|--update]}} {{caminho/para/ponto_de_montagem}}`
