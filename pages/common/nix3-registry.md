# nix registry

> Manage a Nix flake registry.
> See `tldr nix3 flake` for information about flakes.
> More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-registry.html>.

- Pin the `nixpkgs` revision to the current version of the upstream repository:

`nix registry pin {{nixpkgs}}`

- Pin an entry to the latest version of the branch, or a particular reivision of a github repository:

`nix registry pin {{entry}} {{github:owner/repo/branch_or_revision}}`

- Add a new entry that always points to the latest version of a github repository, updating automatically:

`nix registry add {{entry}} {{github:owner/repo}}`

- Remove a registry entry:

`nix registry remove {{entry}}`

- See documentation about what Nix flake registries are:

`nix registry --help`
