# alacritty

> Emulador de terminal multiplataforma acelerado por GPU.
> Mais informações: <https://github.com/alacritty/alacritty>.

- Abre Alacritty numa nova janela:

`alacritty`

- Executa no directório especificado:

`alacritty --working-directory {{caminho/para/diretório}}`

- Executa comando numa nova janela de Alacritty:

`alacritty -e {{comando}}`

- Define um caminho alternativo para o ficheiro de configuração (por omissão `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{caminho/para/configuração.toml}}`

- Executa com carregamento automático de configuração (pode ser definido por omissão em `alacritty.toml`):

`alacritty --live-config-reload --config-file {{caminho/para/configuração.toml}}`
