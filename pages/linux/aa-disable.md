# aa-disable

> Disable AppArmor security policies.
> See also: `aa-complain`, `aa-enforce`, `aa-status`.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Disable profile:

`sudo aa-disable {{path/to/profile1 path/to/profile2 ...}}`

- Disable profiles (defaults to `/etc/apparmor.d`):

`sudo aa-disable --dir {{path/to/profiles}}`
