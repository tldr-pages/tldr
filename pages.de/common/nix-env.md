# nix-env

> Manipulieren oder Abfragen von Nix-Benutzerumgebungen.
> Weitere Informationen: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- Alle installierten Pakete auflisten:

`nix-env -q`

- Installierte Pakete abfragen:

`nix-env -q {{suchbegriff}}`

- Verfügbare Pakete abfragen:

`nix-env -qa {{suchbegriff}}`

- Paket installieren:

`nix-env -iA nixpkgs.{{paket_name}}`

- Installieren eines Pakets von einer URL:

`nix-env -i {{paket_name}} --datei {{beispiel.com}}`

- Paket deinstallieren:

`nix-env -e {{paket_name}}`

- Upgrade eines Pakets:

`nix-env -u {{paket_name}}`

- Alle Pakete aktualisieren:

`nix-env -u`
