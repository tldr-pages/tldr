# koji

> The Fedora Koji build system client.
> More information: <https://pagure.io/koji/>.

- List all available targets:

`koji list-targets`

- Trigger a new build for a specific target using a source RPM (SRPM):

`koji build {{target_name}} {{path/to/package.src.rpm}}`

- Search for packages in Koji:

`koji search package {{package_name}}`

- Show details about a specific build:

`koji buildinfo {{build_id|n-v-r}}`

- Cancel a running task:

`koji cancel {{task_id}}`

- Display help for a subcommand:

`koji help {{subcommand}}`
