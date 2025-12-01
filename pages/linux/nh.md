# nh

> Modern helper utility tool for the Nix/Nixos ecosystem.
> More information: <https://github.com/nix-community/nh>.

- Search for a specific package in Nixpkgs and limit its research to a specified number of items:

`nh search {{[-l|--limit]}} {{number}} {{typeName}}`

- Re-implements the nix-collect-garbage command while also collecting gcroots:

`nh clean all {{[-a|--ask]}}`

- Build the specified nixos flake configuration and open it in a virtual machine:

`nh os build-vm {{path/to/flake}} {{-H|--hostname}} {{myHost}}`

- Build and switch to the specified home-manager flake configuration:

`nh home switch {{path/to/flake}} -C {{myHome}}`

- Build and switch to the specified darwin flake configuration:

`nh darwin switch {{path/to/flake}} {{-H|--hostname}} {{myHost}}`

- Generate specified shell completion files into stdout:

`nh completions {{shellName}}`
