# aa-cleanprof

> Clean AppArmor security profiles by removing unused rules.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-cleanprof.8>.

- Clean a profile to remove unused rules:

`sudo aa-cleanprof {{profile_name}}`

- Clean multiple profiles at once:

`sudo aa-cleanprof {{profile1}} {{profile2}}`

- Run in verbose mode to see detailed output:

`sudo aa-cleanprof --verbose {{profile_name}}`

- Display help information:

`aa-cleanprof --help`
