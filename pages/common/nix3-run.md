# nix run

> Run an application from a Nix flake.
> See also: `nix3 flake` for information about flakes.
> More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-run.html>.

- Run the default application in the flake in the current directory:

`nix run`

- Run a command whose name matches the package name from nixpkgs (if you want a different command from that package, see `tldr nix3 shell`):

`nix run nixpkgs#{{pkg}}`

- Run a command with provided arguments:

`nix run nixpkgs#{{vim}} -- {{path/to/file}}`

- Run from a remote repository:

`nix run {{remote_name}}:{{owner}}/{{repo}}`

- Run from a remote repository using a specific tag, revision or branch:

`nix run {{remote_name}}:{{owner}}/{{repo}}/{{reference}}`

- Run from a remote repository specifying a subdirectory and a program:

`nix run "{{remote_name}}:{{owner}}/{{repo}}?dir={{dir_name}}#{{app}}"`

- Run the flake of a GitHub pull request:

`nix run github:{{owner}}/{{repo}}/pull/{{number}}/head`
