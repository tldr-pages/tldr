# alacritty

> Emulateur de terminal propulsé par GPU, Multi-plateforme.
> Plus d'informations : <https://github.com/alacritty/alacritty>.

- Ouvre une nouvelle fenêtre Alacritty :

`alacritty`

- Lance dans un dossier spécifique :

`alacritty --working-directory {{chemin/vers/dossier}}`

- Lance une commande dans une nouvelle fenêtre Alacritty :

`alacritty -e {{commande}}`

- Utilise un autre fichier de configuration (le fichier par défault étant `$XDG_CONFIG_HOME/alacritty/alacritty.toml`) :

`alacritty --config-file {{chemin/vers/config.toml}}`

- Lance avec la mise à jour en live dès que la configuration est modifiée ( peu également être activé par défaut dans `alacritty.toml`) :

`alacritty --live-config-reload --config-file {{chemin/vers/config.toml}}`
