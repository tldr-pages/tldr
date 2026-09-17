# nh os

> Reconfigure or debug a NixOS machine.
> More information: <https://github.com/nix-community/nh#usage>.

- Build and switch to a specified NixOS flake configuration:

`nh os switch {{path/to/flake}}`

- Update all the flake inputs of the specified NixOS flake configuration, build it and make it the boot default:

`nh os boot {{path/to/flake}} {{[-u|--update]}}`

- Build and activate a specified NixOS flake configuration specialisation:

`nh os test {{path/to/flake}} {{[-s|--specialisation]}} {{specialisation}}`

- Build a specified NixOS flake configuration host and create a symlink of the result from the Nix store in the current directory:

`nh os build-vm {{path/to/flake}} {{[-H|--hostname]}} {{host}}`

- Load a specified NixOS flake configuration in Nix REPL (Nix evaluation environment):

`nh os repl {{path/to/flake}}`

- List all available generations from profile path:

`nh os info`

- Rollback to a specified generation:

`nh os rollback {{[-t|-to]}} {{generation}}`
