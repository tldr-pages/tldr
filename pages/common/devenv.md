# devenv

> Fast, Declarative, Reproducible and Composable Developer Environments using Nix.
> More information: <https://devenv.sh>.

- Initialise the environment:

`devenv init`

- Enter the Development Environment with relaxed hermeticity (state of being airtight):

`devenv shell --impure`

- Get detailed information about the current environment:

`devenv info --verbose`

- Start processes with `devenv`:

`devenv up --config /{{file}}/{{path}}/`

- Clean the environment variables and re-enter the shell in offline mode:

`devenv --clean --offline`

- Delete the previous shell generations:

`devenv gc`
