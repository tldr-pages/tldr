# gh workflow

> List, view, and run GitHub Actions workflows.
> More information: <https://cli.github.com/manual/gh_workflow>.

- Interactively select a workflow to view the latest jobs for:

`gh workflow view`

- View a specific workflow in the default browser:

`gh workflow view {{path/to/file.yml}} --web`

- Display the YAML definition of a specific workflow:

`gh workflow view {{path/to/file.yml}} --yaml`

- Display the YAML definition for a specific Git branch or tag:

`gh workflow view {{path/to/file.yml}} --ref {{branch_or_tag_name}} --yaml`

- List workflow files (use `--all` to include disabled workflows):

`gh workflow list`

- Run a manual workflow with parameters:

`gh workflow run {{path/to/file.yml}} --raw-field {{param1}}={{value1}} --raw-field {{param2}}={{value2}}`

- Run a manual workflow using a specific branch or tag with JSON parameters from `stdin`:

`echo '{{{"param1":"value1", "param2":"value2"}}}' | gh workflow run {{path/to/file.yml}} --ref {{branch_or_tag_name}}`

- Enable or disable a specific workflow:

`gh workflow {{enable|disable}} {{path/to/file.yml}}`
