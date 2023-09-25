# aa-status

> List currently loaded AppArmor modules.
> See also: `aa-complain`, `aa-disable`, `aa-enforce`.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>.

- Check status:

`sudo aa-status`

- Display the number of loaded policies:

`sudo aa-status --profiled`

- Display the number of loaded enforicing policies:

`sudo aa-status --enforced`

- Display the number of loaded non-enforcing policies:

`sudo aa-status --complaining`

- Display the number of loaded enforcing policies that kill tasks:

`sudo aa-status --kill`
