# systemctl mask

> Link units to `/dev/null` so that they can be even started.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#mask%20UNIT%E2%80%A6>.

- Mask a service:

`systemctl mask {{service_name}}`

- Ensure that the service is shut down while masking:

`systemctl mask {{service_name}} --now`

- Mask a user service:

`systemctl mask {{service_name}} --user`
