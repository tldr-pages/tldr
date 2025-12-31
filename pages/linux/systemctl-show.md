# systemctl show

> Show properties of units or systemd itself.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#show%20PATTERN%E2%80%A6%7CJOB%E2%80%A6>.

- Show properties of the system service manager:

`systemctl show`

- Show properties of the user service manager:

`systemctl show --user`

- Show properties of a specific unit:

`systemctl show {{unit}}`

- Show properties of a specific user unit:

`systemctl show {{unit}} --user`

- Include empty properties in the list:

`systemctl show {{[-a|--all]}}`

- Only show the specified properties:

`systemctl show {{unit}} {{[-p|--property]}} {{Wants,Conflicts,...}}`
