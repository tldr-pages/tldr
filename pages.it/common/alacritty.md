# alacritty

> Emulatore di terminale multipiattaforma con accelerazione GPU.
> Maggiori informazioni: <https://manned.org/alacritty>.

- Avvia un nuovo processo Alacritty e crea una finestra:

`alacritty`

- Avvia il demone Alacritty (senza creare una finestra):

`alacritty --daemon`

- Crea una nuova finestra usando il processo Alacritty già in esecuzione:

`alacritty msg create-window`

- Avvia la shell in una directory specifica (funziona anche con `alacritty msg create-window`):

`alacritty --working-directory {{percorso/alla/directory}}`

- Esegui un comando in una nuova finestra Alacritty (funziona anche con `alacritty msg create-window`):

`alacritty {{[-e|--command]}} {{comando}}`

- Usa un file di configurazione alternativo (predefinito: `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{percorso/al/config.toml}}`
