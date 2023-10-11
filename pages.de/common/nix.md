# nix

> Dienstprogramme für die Nix-Sprache und den Nix-Speicher.
> Weitere Informationen: <https://nixos.org>.

- Suche nach einem Paket über seinen Namen oder seine Beschreibung:

`nix search {{suchbegriff}}`

- Starte eine Nix-Shell, die die angegebenen Pakete zur Verfügung stellt:

`nix run {{nixpkgs.pkg1 nixpkgs.pkg2 ...}}`

- Optimiere die Festplattennutzung des Nix-Speichers durch Zusammenfassen doppelter Dateien:

`nix store optimise`

- Starte eine interaktive Umgebung zum Ausführen von Nix-Ausdrücken:

`nix repl`

- Upgrade Nix auf die neueste stabile Version:

`nix upgrade-nix`
