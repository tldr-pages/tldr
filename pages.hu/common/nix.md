# nix

> Segédprogramok a Nix nyelvhez és tárolóhoz. További információ: <https://nixos.org>.

- Egy csomag keresése a neve vagy a leírása alapján:

`nix search {{search_term}}`

- Nix shell indítása a megadott csomagok elérhetőségével:

`nix run {{nixpkgs.pkg1 nixpkgs.pkg2 nixpkgs.pkg3...}}`

- A Nix tároló lemezhasználatának optimalizálása a duplikált fájlok egyesítésével:

`nix store optimise`

- Interaktív környezet indítása a Nix-kifejezések kiértékeléséhez:

`nix repl`

- A Nix frissítése a legújabb stabil verzióra:

`nix upgrade-nix`
