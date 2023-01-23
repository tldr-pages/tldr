# nixos-container

> NixOS konténerek indítása Linux konténerek használatával. További információ: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- Futtatott konténerek listázása:

`sudo nixos-container list`

- NixOS-konténer létrehozása egy adott konfigurációs fájllal:

`sudo nixos-container create {{container_name}} --config-file {{nix_config_file_path}}`

- Egy adott konténer elindítása, leállítása, megszüntetése vagy megsemmisítése:

`sudo nixos-container {{start|stop|terminate|destroy|status}} {{container_name}}`

- Parancs futtatása egy futó konténerben:

`sudo nixos-container run {{container_name}} -- {{command}} {{command_arguments}}`

- Egy konténer konfigurációjának frissítése:

`sudo $EDITOR /var/lib/container/{{container_name}}/etc/nixos/configuration.nix && sudo nixos-container update {{container_name}}`

- Interaktív shell munkamenet belépése egy már futó konténerben:

`sudo nixos-container root-login {{container_name}}`
