# phpbu

> A backup utility framework for PHP.
> More information: <https://phpbu.de/manual/current/en/phpbu-manual.html#cli>.

- Run backups using the default `phpbu.xml` configuration file:

`phpbu`

- Run backups using a specific configuration file:

`phpbu --configuration={{path/to/configuration_file.xml}}`

- Only run the specified backups:

`phpbu --limit={{backup_task_name}}`

- Simulate the actions that would have been performed:

`phpbu --simulate`
