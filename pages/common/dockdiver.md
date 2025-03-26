# dockdiver

> A tool for interacting with Docker registries, including listing and dumping repositories.
> More information: <https://github.com/MachiavelliII/dockdiver>.

- List all repositories in a Docker registry:

`dockdiver -url {{http://target}} -list`

- Dump a specific repository to the default output directory (docker_dump):

`dockdiver -url {{http://target}} -dump {{repository_name}}`

- Dump all repositories with basic authentication:

`dockdiver -url {{http://example.com}} -dump-all -username {{username}} -password {{password}}`

- Dump a repository with a custom port and rate limit:

`dockdiver -url http://example.com -dump {{repository_name}} -port {{port}} -rate {{requests_per_second}} -dir {{path/to/output_directory}}`

- Dump all repositories with bearer token for authorization:

`dockdiver -url {{http://example.com}} -dump-all -bearer {{bearer_token}}`

- Add custom headers as JSON (e.g., '{"X-Custom": "Value"}'):

`dockdiver -url {{http://example.com}} -list -headers {{'{"X-Custom": "Value"}'}}`
