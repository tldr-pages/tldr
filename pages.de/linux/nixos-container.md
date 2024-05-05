# nixos-container

> Startet NixOS Container basierend auf Linux Containern.
> Weitere Informationen: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- Gibt eine Liste der gestarteten Container aus:

`sudo nixos-container list`

- Erstelle einen NixOS Container mit einer spezifischen Konfigurations-Datei:

`sudo nixos-container create {{container_name}} --config-file {{nix_config_file_path}}`

- Starte, stoppe, terminiere oder zerstöre den angegebenen Container:

`sudo nixos-container {{start|stop|terminate|destroy|status}} {{container_name}}`

- Führe ein Kommando in einem laufenden Container aus:

`sudo nixos-container run {{container_name}} -- {{command}} {{command_arguments}}`

- Aktualisiere eine Containerkonfiguration:

`sudo $EDITOR /var/lib/container/{{container_name}}/etc/nixos/configuration.nix && sudo nixos-container update {{container_name}}`

- Starte eine interaktive Shell innerhalb eines laufenden Containers:

`sudo nixos-container root-login {{container_name}}`
