# act

> Execute GitHub Actions locally using Docker.
> More information: <https://github.com/nektos/act>.

- [l]ist the available actions:

`act -l`

- Run the default event:

`act`

- Run a specific event:

`act {{event_type}}`

- Run a specific [a]ction:

`act -a {{action_id}}`

- Do [n]ot actually run the actions (i.e. a dry run):

`act -n`

- Show [v]erbose logs:

`act -v`

- Run a specific [W]orkflow:

`act push -W {{path/to/workflow}}`
