# act

> Execute GitHub Actions locally using Docker.
> More information: <https://manned.org/act>.

- List the available jobs:

`act {{[-l|--list]}}`

- Run the default event:

`act`

- Run a specific event:

`act {{event_type}}`

- Run a specific job:

`act {{[-j|--job]}} {{job_id}}`

- Do [n]ot actually run the actions (i.e. a dry run):

`act {{[-n|--dryrun]}}`

- Show verbose logs:

`act {{[-v|--verbose]}}`

- Run a specific workflow with the push event:

`act push {{[-W|--workflows]}} {{path/to/workflow}}`
