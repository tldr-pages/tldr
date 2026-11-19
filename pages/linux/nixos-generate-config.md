# nixos-generate-config

> Generate NixOS configuration files based on the detected hardware.
> More information: <https://nixos.org/manual/nixos/stable/#sec-installation-manual-installing>.

- Generate `configuration.nix` and `hardware-configuration.nix` in `/etc/nixos`:

`sudo nixos-generate-config`

- Generate the configuration for a system mounted at a specific path (e.g. during installation):

`sudo nixos-generate-config --root {{path/to/mount_point}}`

- Write the configuration files to a specific directory:

`sudo nixos-generate-config --dir {{path/to/directory}}`

- Print the detected hardware configuration without writing any files:

`sudo nixos-generate-config --show-hardware-config`

- Also generate a `flake.nix`:

`sudo nixos-generate-config --flake`

- Overwrite an existing `configuration.nix` (and `flake.nix` if `--flake` is passed):

`sudo nixos-generate-config --force`

- Generate the hardware configuration without file system and swap entries:

`sudo nixos-generate-config --no-filesystems`
