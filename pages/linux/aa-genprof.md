# aa-genprof

> Generate AppArmor security profiles by monitoring program behavior.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-genprof.8>.

- Start generating a profile for a program:

`sudo aa-genprof {{program_path}}`

- Update an existing profile interactively:

`sudo aa-genprof --update {{profile_name}}`

- Display help information:

`aa-genprof --help`
