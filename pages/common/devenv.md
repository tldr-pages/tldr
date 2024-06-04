# devenv

> Fast, Declarative, Reproducible and Composable Developer Environments using Nix.
> More information: <https://devenv.sh>.

- Initialise environment:

`devenv init`

- Enter Development Environment with relaxed hermeticity:

`devenv shell --impure`

- Get detailed information about the current environment:

`devenv info --verbose`

- Start processes with devenv CLI:

`devenv up --config /{{file}}/{{path}}/`

- Clean environment variables and re-enter shell in offline mode:

`devenv --clean --offline`

- Delete previous shell generations:

`devenv gc`
