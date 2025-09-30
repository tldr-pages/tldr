# aa-remove-unknown

> Remove AppArmor profiles that are no longer present in the configuration directory.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-remove-unknown.8>.

- Perform a dry run to see which profiles would be removed:

`sudo aa-remove-unknown -n`

- Actually remove the profiles:

`sudo aa-remove-unknown`

- Display help:

`aa-remove-unknown {{[-h|--help]}}`
