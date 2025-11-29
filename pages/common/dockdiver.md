# dockdiver

> A tool for interacting with Docker registries, including listing and dumping repositories.
> More information: <https://github.com/MachiavelliII/dockdiver#instructions>.

- List all repositories in a Docker registry:

`dockdiver -url {{https://example.com}} -list`

- Dump a specific repository to the default output directory (docker_dump):

`dockdiver -url {{https://example.com}} -dump {{repository_name}}`

- Dump all repositories with basic authentication:

`dockdiver -url {{https://example.com}} -dump-all -username {{username}} -password {{password}}`

- Dump a repository with a rate limit and a custom port (the default port is `5000`):

`dockdiver -url {{https://example.com}} -dump {{repository_name}} -port {{port}} -rate {{requests_per_second}} -dir {{path/to/output_directory}}`

- Dump all repositories with bearer token for authorization:

`dockdiver -url {{https://example.com}} -dump-all -bearer {{bearer_token}}`

- Add custom headers as JSON (e.g., '{"X-Custom": "Value"}'):

`dockdiver -url {{https://example.com}} -list -headers '{{{"X-Custom": "Value"}}}'`
