# nixos-option

> Prüfe eine NixOS Konfiguration.
> Mehr Informationen: <https://nixos.org/manual/nixos/stable/index.html#sec-modularity>.

- Liste alle Unterschlüssel eines angegebenen Options-Schlüssels:

`nixos-option {{option_key}}`

- Liste aktuelle Boot-Kernel Module:

`nixos-option boot.kernelModules`

- Liste Authorisierungs-Schlüssel für einen spezifischen Benutzer:

`nixos-option users.users.{{username}}.openssh.authorizedKeys.{{keyFiles|keys}}`

- Liste alle Remote-Builders:

`nixos-option nix.buildMachines`

- Liste alle Unterschlüssel eines angegebenen Options-Schlüssels innerhalb einer angegebenen Konfigurations-Datei:

`NIXOS_CONFIG={{path_to_configuration.nix}} nixos-option {{option_key}}`

- Zeige rekursiv alle Werte eines Benutzers:

`nixos-option -r users.users.{{user}}`
