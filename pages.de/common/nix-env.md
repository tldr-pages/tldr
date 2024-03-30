# nix-env

> Manipulieren oder Abfragen von Nix-Benutzerumgebungen.
> Weitere Informationen: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- Liste alle installierten Pakete auf:

`nix-env -q`

- Frage installierte Pakete ab:

`nix-env -q {{suchbegriff}}`

- Frage verfügbare Pakete ab:

`nix-env -qa {{suchbegriff}}`

- Installiere Paket:

`nix-env -iA nixpkgs.{{paket_name}}`

- Installiere ein Paket von einer URL:

`nix-env -i {{paket_name}} --file {{beispiel.com}}`

- Deinstalliere ein Paket:

`nix-env -e {{paket_name}}`

- Upgrade ein Pakets:

`nix-env -u {{paket_name}}`

- Upgrade alle Pakete:

`nix-env -u`
