# flexget

> A multipurpose automation tool for content like torrents, nzbs, podcasts, comics, series, movies, etc.
> More information: <https://flexget.com/en/CLI>.

- Run all Flexget tasks now:

`flexget execute --now`

- Start Flexget daemon and daemonize the process:

`flexget daemon start -d`

- List all series recorded in Flexget:

`flexget series list`

- Run task `foo` from config file `bar.yml`:

`flexget -c {{bar.yml}} execute --task {{foo}}`
