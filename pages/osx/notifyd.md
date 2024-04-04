# notifyd

> Notification server.
> It should not be invoked manually.
> More information: <https://keith.github.io/xcode-man-pages/notifyd.8.html>.

- Start the daemon:

`notifyd`

- Log debug messages to the default log file (`/var/log/notifyd.log`):

`notifyd -d`

- Log debug messages to an alternate log file:

`notifyd -d -log_file {{path/to/log_file}}`
