# systemctl log-target

> Get or set the log target for the systemd manager.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#log-target%20[TARGET]>.

- Show the current log target of the systemd manager:

`systemctl log-target`

- Set the manager's log target:

`systemctl log-target {{journal-or-kmsg|journal|kmsg|console|syslog|null|auto}}`
