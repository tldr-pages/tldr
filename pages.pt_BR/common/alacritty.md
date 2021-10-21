# alacritty

> Terminal multiplataforma, acelerado por GPU.
> Mais informações: <https://github.com/alacritty/alacritty>.

- Abre uma nova janela do Alacritty:

`alacritty`

- Roda em um diretório específico:

`alacritty --working-directory {{caminho/para/diretório}}`

- Roda um comando em uma nova janela do Alacritty:

`alacritty -e {{comando}}`

- Especifica um arquivo de configuração alternativo (`$XDG_CONFIG_HOME/alacritty/alacritty.yml` por padrão):

`alacritty --config-file {{caminho/para/config.yml}}`

- Executa com configuração ao vivo habilitada (pode também ser habilitada por padrão no `alacritty.yml`):

`alacritty --live-config-reload --config-file {{caminho/para/config.yml}}`
