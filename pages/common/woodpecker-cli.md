# woodpecker-cli

> Manage, configure, and inspect Woodpecker CI servers, and run workflows locally.
> More information: <https://woodpecker-ci.org/docs/cli>.

- Lint all workflows in the current project:

`woodpecker-cli lint`

- Execute a workflow locally:

`woodpecker-cli exec {{path/to/workflow.yml}}`

- Execute a workflow locally with environment variables:

`woodpecker-cli exec --env {{variable_name}}={{variable_value}} {{path/to/workflow.yml}}`

- Execute a workflow locally with secrets:

`woodpecker-cli exec --secrets {{name}}="{{value}}" {{path/to/workflow.yml}}`

- Execute a workflow locally with multiple secrets:

`woodpecker-cli exec --secrets {{name1="value1",name2="value2",...}} {{path/to/workflow.yml}}`

- Set up the command-line client to manage a Woodpecker CI server:

`woodpecker-cli setup`

- Show recent pipelines that have run on the remote Woodpecker CI server:

`woodpecker-cli pipeline show`

- Update woodpecker-cli to the latest version:

`woodpecker-cli update`
