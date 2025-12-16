# nix flake

> Manage Nix flakes.
> Subcommands such as nix flake `init`, `show`, `info` have their own pages.
> More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-flake.html>.

- Update all inputs (dependencies) of the flake in the current directory:

`nix flake update`

- Update a specific input (dependency) of the flake in the current directory:

`nix flake update {{input}}`

- Clone a Github repository containing a flake:

`nix flake clone {{github:owner/repo#attributes}}`

- Create missing lock file entries for a flake in a specified directory:

`nix flake lock {{path/to/flake}}`

- Display help:

`nix flake --help`
