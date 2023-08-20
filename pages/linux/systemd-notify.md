# systemd-notify

> Notify the service manager about start-up completion and other daemon status changes.
> This command is useless outside systemd service scripts.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-notify.html>.

- Notify systemd that the service has completed its initialization and is fully started. It should be invoked when the service is ready to accept incoming requests:

`systemd-notify --booted`

- Signal to systemd that the service is ready to handle incoming connections or perform its tasks:

`systemd-notify --ready`

- Provide a custom status message to systemd (this information is shown by `systemctl status`):

`systemd-notify --status="{{Add custom status message here...}}"`
