# code

> Visual Studio Code.
> Weitere Informationen: <https://github.com/microsoft/vscode>.

- Öffne Visual Studio Code:

`code`

- Öffne bestimmte Dateien und/oder Verzeichnisse:

`code {{pfad/zu/datei_oder_verzeichnis1 pfad/zu/datei_oder_verzeichnis2 ...}}`

- Vergleiche zwei bestimmte Dateien:

`code --diff {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Öffne bestimmte Dateien und/oder Verzeichnisse in einem neuen Fenster:

`code --new-window {{pfad/zu/datei_oder_verzeichnis1 pfad/zu/datei_oder_verzeichnis2 ...}}`

- Installiere oder lösche bestimmte Erweiterung:

`code --{{install|uninstall}}-extension {{herausgeber.erweiterung}}`

- Liste alle installierten Erweiterungen auf:

`code --list-extensions`

- Liste alle installierten Erweiterungen und deren Version auf:

`code --list-extensions --show-versions`

- Starte Visual Studio Code als Superuser und speichere Benutzerdaten in einem bestimmten Verzeichnis:

`sudo code --user-data-dir {{pfad/zu/verzeichnis}}`
