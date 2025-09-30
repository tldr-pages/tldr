# aa-audit

> Set AppArmor security profiles to audit mode.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-audit.8>.

- Set a profile to audit mode:

`sudo aa-audit {{profile_name}}`

- Set multiple profiles to audit mode:

`sudo aa-audit {{profile1 profile2 ...}}`

- Set a profile to audit mode from a specific directory:

`sudo aa-audit {{[-d|--dir]}} /{{path/to/profiles}} {{profile_name}}`

- Force audit mode even if already applied:

`sudo aa-audit --force {{profile_name}}`

- Set a profile to audit mode without reloading it:

`sudo aa-audit --no-reload {{profile_name}}`

- Remove audit mode for a profile:

`sudo aa-audit {{[-r|--remove]}} {{profile_name}}`

- Display help:

`aa-audit {{[-h|--help]}}`
