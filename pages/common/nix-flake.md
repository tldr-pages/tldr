# nix flake

> Manage Nix flakes.
> More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-flake.html>.

- Create a new flake (just the `flake.nix` file) from the default template, in the current directory:

`nix flake init`

- Update all inputs (dependencies) of the flake in the current directory:

`nix flake update`

- Update a specific input (dependency) of the flake in the current directory:

`nix flake lock --update-input {{input}}`

- Show all the outputs of a flake on github:

`nix flake show {{github:owner/repo}}`

- Display help:

`nix flake --help`
