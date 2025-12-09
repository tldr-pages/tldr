# systemctl soft-reboot

> Shut down and reboot userspace, leaving the kernel running.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#soft-reboot>.

- Perform a soft reboot immediately:

`systemctl soft-reboot`

- Force a soft reboot:

`systemctl soft-reboot --force`

- Schedule a soft reboot for a specific time:

`systemctl soft-reboot --when "{{timestamp}}"`

- Cancel a scheduled soft reboot:

`systemctl soft-reboot --when cancel`
