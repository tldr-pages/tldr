# nix-shell

> Startet eine interaktive Shell, die auf einem Nix-Ausdruck basiert.
> Weitere Informationen: <https://nixos.org/manual/nix/stable/#sec-nix-shell>.

- Start mit Nix-Ausdruck in `shell.nix` oder `default.nix` im aktuellen Verzeichnis:

`nix-shell`

- Shell-Befehl in nicht-interaktiver Shell ausführen und beenden:

`nix-shell --run "{{befehl}} {{arg1 arg2 ...}}"`

- Start mit Ausdruck in `default.nix` im aktuellen Verzeichnis:

`nix-shell {{default.nix}}`

- Start mit aus nixpkgs geladenen Paketen:

`nix-shell --packages {{paket_name_1 paket_name_2 ...}}`

- Start mit Paketen, die aus einer bestimmten Nixpkgs-Revision geladen wurden:

`nix-shell --packages {{paket_name_1 paket_name_2 ...}} -I nixpkgs={{https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz}}`

- Den Rest der Datei mit einem bestimmten Interpreter auswerten, zur Verwendung in `#!-scripts` (siehe <https://nixos.org/manual/nix/stable/#use-as-a-interpreter>):

`nix-shell -i {{interpreter}} --packages {{paket_name_1 paket_name_2 ...}}`
