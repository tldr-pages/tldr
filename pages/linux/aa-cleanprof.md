# aa-cleanprof

> Clean AppArmor security profiles by removing unused rules.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-cleanprof.8>.

- Clean a profile to remove unused rules:

`sudo aa-cleanprof {{profile_name}}`

- Clean multiple profiles at once:

`sudo aa-cleanprof {{profile1 profile2 ...}}`

- Specify the directory containing profiles:

`sudo aa-cleanprof {{[-d|--dir]}} {{/path/to/profiles}} {{profile_name}}`

- Run silently without prompts:

`sudo aa-cleanprof {{[-s|--silent]}} {{profile_name}}`

- Prevent profile reload after cleaning:

`sudo aa-cleanprof --no-reload {{profile_name}}`

- Display help:

`aa-cleanprof {{[-h|--help]}}`
