# nix-collect-garbage

> A nem használt és elérhetetlen nix store elérési útvonalak törlése. A generációkat a `nix-env --list-generations` segítségével lehet listázni. További információ: <https://nixos.org/releases/nix/latest/manual/#sec-nix-collect-garbage>.

- Törölje az egyes profilok aktuális generációi által nem használt összes tárolási útvonalat:

`sudo nix-collect-garbage --delete-old`

- A régi tárolási útvonalak törlésének szimulálása:

`sudo nix-collect-garbage --delete-old --dry-run`

- A 30 napnál régebbi tárolási útvonalak törlése:

`sudo nix-collect-garbage --delete-older-than 30d`
