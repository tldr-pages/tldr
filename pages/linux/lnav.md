# lnav

> Advanced log file viewer to analyze logs with little to no setup.
> More information: <https://docs.lnav.org/en/latest/cli.html>.

- View logs of a program, specifying log files, directories or URLs:

`lnav {{path/to/log_or_directory|url}}`

- View logs of a specific remote host (SSH passwordless login required):

`lnav {{ssh}} {{user}}@{{host1.example.com}}:{{/var/log/syslog.log}}`

- Validate the format of log files against the configuration and report any errors:

`lnav -C {{path/to/log_directory}}`
