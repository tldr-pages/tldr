# nix

> Ein leistungsfähiger Paketmanager, der das Paketmanagement zuverlässig, reproduzierbar und deklarativ macht.
> `nix` ist experimentell und muss gesondert aktiviert werden.
> Einige Unterbefehle wie `build`, `develop`, `flake`, `registry`, `profile`, `search`, `repl`, `store`, `edit`, `why-depends` usw. haben ihre eigene Dokumentation.
> Siehe auch: `nix classic`.
> Weitere Informationen: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix>.

- Aktiviere den `nix` Befehl:

`mkdir {{[-p|--parents]}} ~/.config/nix; echo 'experimental-features = nix-command flakes' > ~/.config/nix/nix.conf`

- Suche ein Paket in nixpkgs nach Namen oder Beschreibung:

`nix search nixpkgs {{suchbegriff}}`

- Starte eine Shell und stelle die angegebenen Pakete von nixpkgs darin bereit:

`nix shell {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- Installiere einige Pakete von nixpkgs dauerhaft:

`nix profile install {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- Entferne ungenutzte Pfade aus dem Nix-Store, um Speicherplatz freizugeben:

`nix store gc`

- Starte eine interaktive Umgebung zur Auswertung von Nix-Ausdrücken:

`nix repl`

- Zeige Hilfe für einen bestimmten Unterbefehl an:

`nix help {{unterbefehl}}`
