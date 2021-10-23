# nixos-container

> Starts NixOS containers using Linux containers.
> More information: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- List running containers:

`sudo nixos-container list`

- Create a NixOS container with a specific configuration file:

`sudo nixos-container create {{container_name}} --config-file {{nix_config_file_path}}`

- Start/stop/terminate/destroy a specific container:

`sudo nixos-container {{start|stop|terminate|destroy|status}} {{container_name}}`

- Run a command in the container:

`sudo nixos-container run {{container_name}} -- {{command}}`

- Update a container configuration:

`sudo $EDITOR /var/lib/container/{{container_name}}/etc/nixos/configuration.nix && sudo nixos-container update {{container_name}}`

- Enter in a container:

`sudo nixos-container root-login {{container_name}}`
