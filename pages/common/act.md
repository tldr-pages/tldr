# act

> Execute GitHub Actions locally using Docker.
> More information: <https://github.com/nektos/act>.

- List the available actions:

`act -l`

- Run the default event:

`act`

- Run a specific event:

`act {{event_type}}`

- Run a specific action:

`act -a {{action_id}}`

- Do not actually run the actions (i.e. a dry run):

`act -n`

- Show verbose logs:

`act -v`

- Run a specific workflow:

`act push -W {{path/to/workflow}}`
