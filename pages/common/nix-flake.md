# nix flake

> Manage Nix flakes.
> Some subcommands such as `init`, `show`, `info` have their own usage documentation.
> More information: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-flake.html>.

- Update all inputs (dependencies) of the flake in the current directory:

`nix flake update`

- Update a specific input (dependency) of the flake in the current directory:

`nix flake update {{input}}`

- Clone a GitHub repository containing a flake:

`nix flake clone {{github:owner/repo#attributes}}`

- Create missing lock file entries for a flake in a specified directory:

`nix flake lock {{path/to/flake}}`

- Display help:

`nix flake --help`
