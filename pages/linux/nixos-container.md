# nixos-container

> Starts NixOS containers using Linux containers.
> More information: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- List running containers:

`sudo nixos-container list`

- Create a NixOS container with a specific configuration file:

`sudo nixos-container create {{container_name}} --config-file {{nix_config_file_path}}`

- Start, stop, terminate, or destroy a specific container:

`sudo nixos-container {{start|stop|terminate|destroy|status}} {{container_name}}`

- Run a command in a running container:

`sudo nixos-container run {{container_name}} -- {{command}} {{command_arguments}}`

- Update a container configuration:

`sudo $EDITOR /var/lib/container/{{container_name}}/etc/nixos/configuration.nix && sudo nixos-container update {{container_name}}`

- Enter an interactive shell session on an already-running container:

`sudo nixos-container root-login {{container_name}}`
