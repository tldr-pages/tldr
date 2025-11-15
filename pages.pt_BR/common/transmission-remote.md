# transmission-remote

> Utilitário de controle remoto para `transmission-daemon` e `transmission`.
> Mais informações: <https://manned.org/transmission-remote>.

- Adiciona um arquivo torrent ou link magnético para o Transmission e baixa para um diretório específico:

`transmission-remote {{hostname}} {{[-a|--all]}} {{torrent|url}} {{[-w|--download-dir]}} {{/caminho/para/diretorio_download}}`

- Altera o diretório de download padrão:

`transmission-remote {{hostname}} {{[-w|--download-dir]}} {{/caminho/para/diretorio_download}}`

- Lista todos os torrents:

`transmission-remote {{hostname}} {{[-l|--list]}}`

- Inicia os torrents 1 e 2, interrompe o torrent 3:

`transmission-remote {{hostname}} {{[-t|--torrent]}} "1,2" {{[-s|--start]}} {{[-t|--torrent]}} 3 {{[-S|--stop]}}`

- Remove os torrents 1 e 2 e também exclui dados locais do torrent 2:

`transmission-remote {{hostname}} {{[-t|--torrent]}} 1 {{[-r|--remove]}} {{[-t|--torrent]}} 2 {{[-rad|--remove-and-delete]}}`

- Interrompe todos os torrents:

`transmission-remote {{hostname}} {{[-t|--torrent]}} {{all}} {{[-S|--stop]}}`

- Move os torrents 1-10 e 15-20 para um novo diretório (que será criado se não existir):

`transmission-remote {{hostname}} {{[-t|--torrent]}} "1-10,15-20" --move {{/caminho/para/nodo_diretorio}}`
