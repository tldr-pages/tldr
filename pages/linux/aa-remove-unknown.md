# aa-remove-unknown

> Remove AppArmor profiles that are no longer present in the configuration directory.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-remove-unknown.8>.

- Simulate removing profiles and display which ones would be removed:

`sudo aa-remove-unknown -n`

- Actually remove the profiles:

`sudo aa-remove-unknown`

- Display help:

`aa-remove-unknown {{[-h|--help]}}`
