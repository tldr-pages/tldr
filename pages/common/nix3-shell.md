# nix shell

> Start a shell in which the specified packages are available.
> Not to be confused with `nix-shell` (see `tldr nix-shell`).
> See `tldr nix3 flake` for information about flakes.

- Start an interactive shell with some packages from `nixpkgs`:

`nix shell {{nixpkgs#pkg1 nixpkgs#packageSet.pkg2 ...}}`

- Start a shell providing a package from an older version of `nixpkgs` (21.05):

`nix shell {{nixpkgs/nixos-21.05#pkg}}`

- Start a shell with the "default package" from a flake in the current directory, printing build logs if any builds happen:

`nix shell -L`

- Start a shell with a package from a flake on GitHub:

`nix shell {{github:owner/repo#pkg}}`

- Run a command in a shell with a package:

`nix shell {{nixpkgs#pkg}} -c {{some-cmd --someflag 'Some other arguments'}}`
