# nix flake show

> Show outputs provided by a flake.
> More information: <https://nix.dev/manual/nix/2.28/command-ref/new-cli/nix3-flake-show.html>.

- Show all the outputs of the flake in the current directory:

`nix flake show`

- Show all the outputs of a flake on Github and print the output as json on a single line:

`nix flake show {{github:owner/repo}} --json --no-pretty`

- Show all the `legacyPackages` outputs of a flake on Github and print the output as multi-line indented json:

`nix flake show {{github:owner/repo}} --json --pretty --legacy`

- List all available flake templates for `nix flake init`:

`nix flake show templates`
