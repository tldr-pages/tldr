# nixos-option

> Inspect a NixOS configuration.
> More information: <https://nixos.org/manual/nixos/stable/index.html#sec-modularity>.

- List all subkeys of a given option key:

`nixos-option {{option_key}}`

- List current boot kernel modules:

`nixos-option boot.kernelModules`

- List authorized keys for a specific user:

`nixos-option users.users.{{username}}.openssh.authorizedKeys.{{keyFiles|keys}}`

- List all remote builders:

`nixos-option nix.buildMachines`

- List all subkeys of a given key on another NixOS configuration:

`NIXOS_CONFIG={{path_to_configuration.nix}} nixos-option {{option_key}}`

- Show recursively all values of a user:

`nixos-option -r users.users.{{user}}`
