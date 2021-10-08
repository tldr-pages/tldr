# alacritty

> Terminal multiplataforma, acelerado por GPU.
> Mais informações: <https://github.com/alacritty/alacritty>.

- Abrir uma nova janela do Alacritty:

`alacritty`

- Rodar em um diretório específico:

`alacritty --working-directory {{caminho/para/o/diretório}}`

- Rodar um comando em uma nova janela do Alacritty:

`alacritty -e {{comando}}`

- Especificar um arquivo de configuração alternativo (`$XDG_CONFIG_HOME/alacritty/alacritty.yml` por padrão):

`alacritty --config-file {{caminho/para/config.yml}}`

- Executar com configuração ao vivo habilitada (pode também ser habilitada por padrão no `alacritty.yml`):

`alacritty --live-config-reload --config-file {{caminho/para/config.yml}}`
