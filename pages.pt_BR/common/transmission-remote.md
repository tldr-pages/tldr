# transmission-remote

> Utilitário de controle remoto para `transmission-daemon` e `transmission`.
> Mais informações: <https://transmissionbt.com>.

- Adiciona um arquivo torrent ou link magnético para o Transmission e baixa para um diretório específico:

`transmission-remote {{hostname}} -a {{torrent|url}} -w {{/caminho/para/diretorio_download}}`

- Altera o diretório de download padrão:

`transmission-remote {{hostname}} -w {{/caminho/para/diretorio_download}}`

- Lista todos os torrents:

`transmission-remote {{hostname}} --list`

- Inicia os torrents 1 e 2, interrompe o torrent 3:

`transmission-remote {{hostname}} -t "{{1,2}}" --start -t {{3}} --stop`

- Remove os torrents 1 e 2 e também exclui dados locais do torrent 2:

`transmission-remote {{hostname}} -t {{1}} --remove -t {{2}} --remove-and-delete`

- Interrompe todos os torrents:

`transmission-remote {{hostname}} -t {{all}} --stop`

- Move os torrents 1-10 e 15-20 para um novo diretório (que será criado se não existir):

`transmission-remote {{hostname}} -t "{{1-10,15-20}}" --move {{/caminho/para/nodo_diretorio}}`
