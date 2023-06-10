# nix-shell

> Start an interactive shell based on a Nix expression.
> See also: `tldr nix3 shell`.
> More information: <https://nixos.org/manual/nix/stable/command-ref/nix-shell.html>.

- Start with nix expression in `shell.nix` or `default.nix` in the current directory:

`nix-shell`

- Run shell command in non-interactive shell and exit:

`nix-shell --run "{{command}} {{argument1 argument2 ...}}"`

- Start with expression in `default.nix` in the current directory:

`nix-shell {{default.nix}}`

- Start with packages loaded from nixpkgs:

`nix-shell --packages {{package1 package2 ...}}`

- Start with packages loaded from specific nixpkgs revision:

`nix-shell --packages {{package1 package2 ...}} -I nixpkgs={{https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz}}`

- Evaluate rest of file in specific interpreter, for use in `#!-scripts` (see <https://nixos.org/manual/nix/stable/#use-as-a-interpreter>):

`nix-shell -i {{interpreter}} --packages {{package1 package2 ...}}`
