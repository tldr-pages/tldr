# nix-env

> Manipulieren oder Abfragen von Nix-Benutzerumgebungen.
> Weitere Informationen: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- Alle installierten Pakete auflisten:

`nix-env -q`

- Installierte Pakete abfragen:

`nix-env -q {{search_term}}`

- Verfügbare Pakete abfragen:

`nix-env -qa {{Suche_Begriff}}`

- Paket installieren:

`nix-env -iA nixpkgs.{{pkg_name}}`

- Installieren eines Pakets von einer URL:

`nix-env -i {{pkg_name}} --datei {{beispiel.com}}`

- Paket deinstallieren:

`nix-env -e {{pkg_name}}`

- Upgrade eines Pakets:

`nix-env -u {{pkg_name}}`

- Alle Pakete aktualisieren:

`nix-env -u`
