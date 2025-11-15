# zapier

> Create, automate, and manage zapier integrations.
> Some subcommands such as `build`, `init`, `scaffold`, `push`, `test`, etc. have their own usage documentation.
> More information: <https://platform.zapier.com/reference/cli>.

- Connect to a Zapier account:

`zapier login`

- Initialize a new Zapier integration with a project template:

`zapier init {{path/to/directory}}`

- Add a starting trigger, create, search, or resource to your integration:

`zapier scaffold {{trigger|create|search|resource}} {{name}}`

- Test an integration:

`zapier test`

- Build and upload an integration to Zapier:

`zapier push`

- Display help:

`zapier help`

- Display help for a specific command:

`zapier help {{command}}`
