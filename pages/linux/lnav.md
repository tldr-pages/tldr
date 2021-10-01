# lnav

> Advanced log file viewer to analyze logs with little to no setup.
> More information: <https://docs.lnav.org/en/latest/cli.html>.

- View logs of a program, the arguments can be log files, directories or URLs:

`lnav {{path/to/logdir}}`

- View logs of remote host host1.example.com (SSH passwordless login required):

`lnav {{ssh user@host1.example.com:/var/log/syslog.log}}`

- Validate log format of log files against the configuration and report any errors:

`lnav -C {{path/to/logdir}}`
