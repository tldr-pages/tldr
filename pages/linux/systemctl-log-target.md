# systemctl log-target

> Get or set the log target for the systemd manager.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#log-target%20%5BTARGET%5D>.

- Show the current log target of the systemd manager:

`systemctl log-target`

- Set the manager's log target:

`systemctl log-target {{journal-or-kmsg|journal|kmsg|console|syslog|null|auto}}`
