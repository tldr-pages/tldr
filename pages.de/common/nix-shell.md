# nix-shell

> Startet eine interaktive Shell, die auf einem Nix-Ausdruck basiert.
> Weitere Informationen: <https://nixos.org/manual/nix/stable/#sec-nix-shell>.

- Starte mit Nix-Ausdruck in `shell.nix` oder `default.nix` im aktuellen Verzeichnis:

`nix-shell`

- Führe Shell-Befehl in nicht-interaktiver Shell aus und beende:

`nix-shell --run "{{befehl}} {{arg1 arg2 ...}}"`

- Starte mit Ausdruck in `default.nix` im aktuellen Verzeichnis:

`nix-shell {{default.nix}}`

- Starte mit aus nixpkgs geladenen Paketen:

`nix-shell --packages {{paket_name_1 paket_name_2 ...}}`

- Starte mit Paketen, die aus einer bestimmten Nixpkgs-Revision geladen wurden:

`nix-shell --packages {{paket_name_1 paket_name_2 ...}} -I nixpkgs={{https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz}}`

- Führe den Rest der Datei mit einem bestimmten Interpreter aus, zur Verwendung in `#!-scripts` (siehe <https://nixos.org/manual/nix/stable/#use-as-a-interpreter>):

`nix-shell -i {{interpreter}} --packages {{paket_name_1 paket_name_2 ...}}`
