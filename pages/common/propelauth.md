# propelauth

> Set up PropelAuth in your application as quickly and easily as possible.
> More information: <https://docs.propelauth.com/reference/api/cli>.

- Login to PropelAuth using an API Key generated from <https://auth.propelauth.com/api_keys/personal>:

`propelauth login`

- Set the default PropelAuth Project to use with the CLI. If no default project is set, you will be prompted to select a Project each time you run certain commands:

`propelauth set-default-project`

- Set up PropelAuth authentication in your project. If no directory is provided, the current directory is used:

`propelauth setup {{[-f|--framework]}} {{path/to/directory}}`

- Log the CLI out of PropelAuth:

`propelauth logout`
