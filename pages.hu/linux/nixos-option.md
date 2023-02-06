# nixos-option

> A NixOS-konfiguráció vizsgálata. További információ: <https://nixos.org/manual/nixos/stable/index.html#sec-modularity>.

- Egy adott opciós kulcs összes alkulcsának listázása:

`nixos-option {{option_key}}`

- Az aktuális boot kernelmodulok listázása:

`nixos-option boot.kernelModules`

- Egy adott felhasználó engedélyezett kulcsainak listája:

`nixos-option users.users.{{username}}.openssh.authorizedKeys.{{keyFiles|keys}}`

- Az összes távoli építők listája:

`nixos-option nix.buildMachines`

- Egy adott kulcs összes alkulcsának listázása egy másik NixOS-konfigurációban:

`NIXOS_CONFIG={{path_to_configuration.nix}} nixos-option {{option_key}}`

- Egy felhasználó összes értékének rekurzív megjelenítése:

`nixos-option -r users.users.{{user}}`
