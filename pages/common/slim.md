# slim

> Analyze and optimize Docker images.
> More information: <https://github.com/slimtoolkit/slim#usage-details>.

- Start Slim on interactive mode:

`slim`

- Analyze Docker layers from a specific image:

`slim xray --target {{image:tag}}`

- Lint a Dockerfile:

`slim lint --target {{path/to/Dockerfile}}`

- Analyze and generate an optimized Docker image:

`slim build {{image:tag}}`

- Display help for a subcommand:

`slim {{subcommand}} --help`
