# nixos-option

> Prüfe eine NixOS Konfiguration.
> Weitere Informationen: <https://nixos.org/manual/nixos/stable/index.html#sec-modularity>.

- Liste alle Unterschlüssel eines angegebenen Options-Schlüssels:

`nixos-option {{option_key}}`

- Liste aktuelle Boot-Kernelmodule:

`nixos-option boot.kernelModules`

- Liste Authorisierungsschlüssel für einen spezifischen Benutzer:

`nixos-option users.users.{{username}}.openssh.authorizedKeys.{{keyFiles|keys}}`

- Liste alle Remote-Builder-Maschinen:

`nixos-option nix.buildMachines`

- Liste alle Unterschlüssel eines angegebenen Options-Schlüssels innerhalb einer angegebenen Konfigurations-Datei:

`NIXOS_CONFIG={{path_to_configuration.nix}} nixos-option {{option_key}}`

- Zeige rekursiv alle Werte eines Benutzers:

`nixos-option -r users.users.{{user}}`
