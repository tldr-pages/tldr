# bk

> Manage Buildkite builds, pipelines, and agents.
> More information: <https://github.com/buildkite/cli#usage>.

- Configure the API token and organization:

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
