# emond

> Event Monitor service that accepts events from various services, runs them through a simple rules engine, and takes action.
> The actions can run commands, send email, or SMS messages.
> More information: <https://keith.github.io/xcode-man-pages/emond.8.html>.

- Start the daemon:

`emond`

- Specify rules for emond to process by giving a path to a file or directory:

`emond -r {{path/to/file_or_directory}}`

- Use a specific configuration file:

`emond -c {{path/to/config_file}}`
