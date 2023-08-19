# systemd-notify

>  Notify service manager about start-up completion and other daemon status changes
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-notify.html#>

- The command is used to notify systemd that the service has completed its initialization and is fully started. It should be invoked when the service is ready to accept incoming requests.

`systemd-notify --booted`

- Used to signal to systemd that the service is ready to handle incoming connections or perform its tasks.

`systemd-notify --ready`

- command allows you to provide a custom status message to systemd. It can be used to provide additional information about the service's initialization progress or state

`systemd-notify --status="Add custom status message here..."`





