# nix

> Dienstprogramme für die Nix-Sprache und den Nix-Speicher.
> Weitere Informationen: <https://nixos.org>.

- Suche nach einem Paket über seinen Namen oder seine Beschreibung:

`nix search {{suchbegriff}}`

- Starten einer Nix-Shell, die die angegebenen Pakete zur Verfügung stellt:

`nix run {{nixpkgs.pkg1 nixpkgs.pkg2 ...}}`

- Optimieren der Festplattennutzung des Nix-Speicher durch Zusammenfassen doppelter Dateien:

`nix store optimise`

- Starten einer interaktiven Umgebung für die Auswertung von Nix-Ausdrücken:

`nix repl`

- Upgrade von Nix auf die neueste stabile Version:

`nix upgrade-nix`
