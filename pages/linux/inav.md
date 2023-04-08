# Inav

> Advanced log file viewer for the console.
> More information: <https://docs.lnav.org/en/latest/>.

- Load and follow the system syslog file:

`inav`

- Load all of the files in `/var/log`:

`inav /var/log`

- To load all of the files in /var/log:

`make 2>&1 | inav -t`
