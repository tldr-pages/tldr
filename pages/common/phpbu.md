# phpbu

> A backup utility framework for PHP.
> More information: <https://phpbu.de>.

- Run backups using the default "phpbu.xml" file:

`phpbu`

- Run backups using a specific configuration file:

`phpbu --configuration={{path/to/configuration_file.xml}}`

- Only run the specified backups:

`phpbu --limit={{backup_task_name}}`

- Don't actually create the backups:

`phpbu --simulate`