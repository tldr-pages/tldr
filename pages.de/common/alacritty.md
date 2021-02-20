# alacritty

> Plattformübergreifender, GPU-beschleunigter Terminalemulator.
> Mehr Informationen: <https://github.com/jwilm/alacritty>.

- Öffne ein neues alacritty-Fenster:

`alacritty`

- Starte alacritty in einem bestimmten Arbeitsverzeichnis:

`alacritty --working-directory {{pfad/zu/verzeichnis}}`

- Führe einen Befehl in einem neuen alacritty-Fenster aus:

`alacritty -e {{befehl}}`

- Gib eine alternative Konfigurations-Datei an (ist standardmäßig $XDG_CONFIG_HOME/alacritty/alacritty.yml):

`alacritty --config-file {{pfad/zu/konfiguration.yml}}`

- Starte mit aktiviertem Live-Konfigurations-Neuladen (kann auch standardmäßig in alacritty.yml eingestellt werden):

`alacritty --live-config-reload --config-file {{pfad/zu/konfiguration.yml}}`
