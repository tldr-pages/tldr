# nix-shell

> Interaktív héj indítása egy Nix-kifejezés alapján. További információ: <https://nixos.org/manual/nix/stable/#sec-nix-shell>.

- Indítsa el a Nix-kifejezéssel a `shell.nix` vagy a `default.nix` címen az aktuális könyvtárban:

`nix-shell`

- Shell parancs futtatása nem interaktív shellben és kilépés:

`nix-shell --run "{{command}} {{arg1 arg2 ...}}"`

- Indítás az aktuális könyvtárban található `default.nix` kifejezéssel:

`nix-shell {{default.nix}}`

- Indítás a nixpkgs-ből betöltött csomagokkal:

`nix-shell --packages {{package_name_1 package_name_2 ...}}`

- Indítás egy adott nixpkgs revízióból betöltött csomagokkal:

`nix-shell --packages {{package_name_1 package_name_2 ...}} -I nixpkgs={{https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz}}`

- A fájl többi részének kiértékelése egy adott értelmezőben, a `#!-scripts` -ban való használathoz ( [lásd https://nixos.org/manual/nix/stable/#use-as-a-interpreter](https://nixos.org/manual/nix/stable/#use-as-a-interpreter)):

`nix-shell -i {{interpreter}} --packages {{package_name_1 package_name_2 ...}}`
