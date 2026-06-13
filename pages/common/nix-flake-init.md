# nix flake init

> Create a flake in the current directory from a template.
> More information: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-flake-init.html>.

- Create a new flake from the default template, in the current directory:

`nix flake init`

- Create a new flake with a specified template (see `nix flake show` for information about templates):

`nix flake init {{[-t|--template]}} templates#{{your_template}}`
