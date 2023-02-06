# nix-env

> Nix felhasználói környezetek kezelése vagy lekérdezése. További információ: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- Az összes telepített csomag listázása:

`nix-env -q`

- A telepített csomagok lekérdezése:

`nix-env -q {{search_term}}`

- Elérhető csomagok lekérdezése:

`nix-env -qa {{search_term}}`

- Csomag telepítése:

`nix-env -iA nixpkgs.{{pkg_name}}`

- Csomag telepítése egy URL-címről:

`nix-env -i {{pkg_name}} --file {{example.com}}`

- Csomag eltávolítása:

`nix-env -e {{pkg_name}}`

- Egy csomag frissítése:

`nix-env -u {{pkg_name}}`

- Az összes csomag frissítése:

`nix-env -u`
