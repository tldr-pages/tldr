# nixos-container

> Startet NixOS Container basierend auf Linux Containern.
> Mehr Informationen: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- Gestartete Container listen:

`sudo nixos-container list`

- Erstelle einen NixOS Container mit einer spezifischen Konfigurations-Datei:

`sudo nixos-container create {{container_name}} --config-file {{nix_config_file_path}}`

- Start, Stoppe, Terminiere oder zerstöre einen spezifischen Container:

`sudo nixos-container {{start|stop|terminate|destroy|status}} {{container_name}}`

- Starte einen Command in einem laufenden Container:

`sudo nixos-container run {{container_name}} -- {{command}} {{command_arguments}}`

- Aktualisiere eine Container Konfiguration:

`sudo $EDITOR /var/lib/container/{{container_name}}/etc/nixos/configuration.nix && sudo nixos-container update {{container_name}}`

- Starte und wechsle in eine interaktive Shell innerhalb eines laufenden Containers:

`sudo nixos-container root-login {{container_name}}`
