# alacritty

> Plattformübergreifender, GPU-beschleunigter Terminalemulator.
> Weitere Informationen: <https://github.com/alacritty/alacritty>.

- Öffne ein neues Alacritty-Fenster:

`alacritty`

- Starte Alacritty in einem bestimmten Arbeitsverzeichnis:

`alacritty --working-directory {{pfad/zu/verzeichnis}}`

- Führe einen Befehl in einem neuen Alacritty-Fenster aus:

`alacritty -e {{befehl}}`

- Gib eine alternative Konfigurations-Datei an (ist standardmäßig `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{pfad/zu/konfiguration.toml}}`

- Starte mit aktiviertem Live-Konfigurations-Neuladen (kann auch standardmäßig in `alacritty.toml` eingestellt werden):

`alacritty --live-config-reload --config-file {{pfad/zu/konfiguration.toml}}`
