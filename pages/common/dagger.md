# dagger

> Programmable CI/CD engine that runs pipelines in containers locally, in CI, or in the cloud.
> More information: <https://docs.dagger.io/reference/cli>.

- Initialize a new module with the specified SDK:

`dagger init --sdk {{go|python|typescript}} {{path/to/module}}`

- Prepare a local module for development:

`dagger develop`

- List available functions in the current module:

`dagger functions`

- Call a function on the current module:

`dagger call {{function_name}}`

- Install a module dependency from a Git repository:

`dagger install {{github.com/user/repo}}`

- Update a module's dependencies:

`dagger update`

- Display help:

`dagger {{[-h|--help]}}`

- Display version:

`dagger version`
