# envoy

> A PHP-based task manager for Laravel remote servers.
> More information: <https://laravel.com/docs/envoy>.

- Initialize a configuration file:

`envoy init {{host_name}}`

- Run a task:

`envoy run {{task_name}}`

- Run a task from a specific project:

`envoy run --path {{path/to/directory}} {{task_name}}`

- Run a task and continue on failure:

`envoy run --continue {{task_name}}`

- Dump a task as a Bash script for inspection:

`envoy run --pretend {{task_name}}`

- Connect to the specified server via SSH:

`envoy ssh {{server_name}}`
