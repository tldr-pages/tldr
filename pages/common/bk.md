# bk

> Manage Buildkite builds, pipelines, and agents.
> Some subcommands such as `build`, `pipeline`, and `agent` have their own usage documentation.
> More information: <https://github.com/buildkite/cli>.

- Configure with your organization and API token:

`bk configure`

- Select an organization to use:

`bk use {{organization_slug}}`

- Initialize a `pipeline.yaml` file:

`bk init`

- List all pipelines in the current organization:

`bk pipeline list`

- Trigger a build for a pipeline:

`bk build create {{pipeline_slug}}`

- View the status of a specific build:

`bk build view {{build_number}}`

- List all agents in the current organization:

`bk agent list`

- Display help:

`bk {{[-h|--help]}}`
