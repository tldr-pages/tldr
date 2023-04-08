# Inav

> An advanced log file viewer for the small-scale.
> More information: <https://docs.lnav.org/en/latest/>.

- Load and follow the system syslog file:

`inav`

- Load all of the files in `/var/log`:

`inav /var/log`

- To load all of the files in /var/log:

`make 2>&1 | inav -t`
