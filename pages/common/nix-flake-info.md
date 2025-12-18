# nix flake info

> Show flake metadata.
> More information: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-flake-info>.

- Show flake metadata of the flake in the current directory:

`nix flake info`

- Show flake metadata from GitHub as a json on a single line:

`nix flake info {{github:owner/repo}} --json --no-pretty`

- Show flake metadata from Github as a multi-line indented json:

`nix flake info {{github:owner/repo}} --json --pretty`
