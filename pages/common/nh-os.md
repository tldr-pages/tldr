# nh

> Modern helper utility tool for the Nix/Nixos ecosystem.
> More information: <https://github.com/nix-community/nh#usage>.

- Build and switch to a specified Nixos flake configuration:

`nh os switch {{path/to/flake}}`

- Update all the flake inputs of the specified Nixos flake configuration, build it and make it the boot default:

`nh os boot {{path/to/flake}} {{[-u|--update]}}`

- Build and activate a specified Nixos flake configuration specialisation:

`nh os test {{path/to/flake}} {{[-s|--specialisation]}} {{specialisation}}`

- Build a specified Nixos flake configuration host and create a symlink of the result from the Nix store in the current directory:

`nh os build-vm {{path/to/flake}} {{[-H|--hostname]}} {{host}}`

- Load a specified nixos flake configuration in repl (nix evaluation environnement):

`nh os repl {{path/to/flake}}`

- List all available generations from profile path:

`nh os info`

- Rollback to a specified generation:

`nh os rollback {{[-t|-to]}} {{generation}}`
