# systemctl-halt

> Shut down and halt the system (stop the OS kernel but keep hardware powered on).
> See also: `halt`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#halt>.

- Halt the system:

`systemctl halt`

- Halt the system immediately without asking services to stop gracefully:

`systemctl halt --force`

- Halt the system immediately without sending notifications to logged-in users:

`systemctl halt --force --no-wall`

- Halt the system immediately without terminating any processes or unmounting filesystems (dangerous, may cause data loss):

`systemctl halt --force --force`

- Schedule a halt at a specific time (e.g., 23:00):

`systemctl halt --when 23:00`

- Schedule a halt after a certain duration (e.g., 2 hours):

`systemctl halt --when +2h`

- Cancel a scheduled halt:

`systemctl halt --when cancel`
