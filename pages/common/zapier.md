# zapier

> Create, automate, and manage zapier integrations.
> Some subcommands such as `build` have their own usage documentation.
> More information: <https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md>.

- Connect to your Zapier account:

`zapier login`

- Initialize a new Zapier integration with a project template:

`zapier init {{path/to/directory}}`

- Add a starting trigger, create, search, or resource to your integration:

`zapier scaffold {{trigger|create|search|resource}} {{name}}`

- Test your integration:

`zapier test`

- Build and upload your integration to Zapier:

`zapier push`

- Display help:

`zapier help`

- Display help for a specific command:

`zapier help {{command}}`
