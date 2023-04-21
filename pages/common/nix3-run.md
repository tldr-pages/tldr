# nix run

> Run an application from a Nix flake.
> See `tldr nix3 flake` for information about flakes.
> More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-run.html>.

- Run a command whose name matches the package name from nixpkgs (if you want a different command from that package, see `tldr nix3 shell`):

`nix run nixpkgs#{{pkg}}`

- Run the default application in the flake in the current directory:

`nix run`
