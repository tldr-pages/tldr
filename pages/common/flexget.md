# flexget

> A multipurpose automation tool for content like torrents, nzbs, podcasts, comics, series, movies, etc.
> More information: <https://flexget.com/en/CLI>.

- Run all Flexget tasks now:

`flexget execute --now`

- Start the Flexget daemon and daemonize its process:

`flexget daemon start --daemonize`

- List all series recorded in Flexget:

`flexget series list`

- Run a task from a configuration file:

`flexget -c {{path/to/config.yml}} execute --task {{task_name}}`
