# transmission-daemon

> Daemon controlado com `transmission-remote` ou sua interface web.
> Veja também: `transmission`.
> Mais informações: <https://manned.org/transmission-daemon>.

- Inicia uma sessão headless `transmission`:

`transmission-daemon`

- Inicia e acompanha um diretório específico por novos torrents:

`transmission-daemon --watch-dir {{caminho/para/diretorio}}`

- Despeja configurações do daemon em formato JSON:

`transmission-daemon --dump-settings > {{caminho/para/arquivo.json}}`

- Inicia com configurações específicas para a interface web:

`transmission-daemon --auth --username {{usuario}} --password {{senha}} --port {{9091}} --allowed {{127.0.0.1}}`
