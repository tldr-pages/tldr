# alacritty

> Emulador de terminal multiplataforma acelerado por GPU.
> Mais informações: <https://github.com/alacritty/alacritty>.

- Abrir Alacritty numa nova janela:

`alacritty`

- Executar na directoria especificada:

`alacritty --working-directory {{caminho/para/directoria}}`

- Executar commando numa nova janela de Alacritty:

`alacritty -e {{comando}}`

- Definir caminho alternativo para o ficheiro de configuração (por omissão `$XDG_CONFIG_HOME/alacritty/alacritty.yml`):

`alacritty --config-file {{caminho/para/configuração.yml}}`

- Executar com carregamento automático de configuração (pode ser definido por omissão em `alacritty.yml`):

`alacritty --live-config-reload --config-file {{caminho/para/configuração.yml}}`
