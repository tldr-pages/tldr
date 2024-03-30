# act

> Execute GitHub Actions locally using Docker.
> More information: <https://github.com/nektos/act>.

- [l]ist the available jobs:

`act -l`

- Run the default event:

`act`

- Run a specific event:

`act {{event_type}}`

- Run a specific [j]ob:

`act -j {{job_id}}`

- Do [n]ot actually run the actions (i.e. a dry run):

`act -n`

- Show [v]erbose logs:

`act -v`

- Run a specific [W]orkflow with the push event:

`act push -W {{path/to/workflow}}`
