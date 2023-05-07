# nix search

> Search for packages in a Nix flake.
> See `tldr nix3 flake` for information about flakes.
> More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-search.html>.

- Search `nixpkgs` for a package based on its name or description:

`nix search {{nixpkgs}} {{search_term...}}`

- Show description of a package from nixpkgs:

`nix search {{nixpkgs#pkg}}`

- Show all packages available from a flake on github:

`nix search {{github:owner/repo}}`
