# apparmor_parser

> Load, compile, and manage AppArmor security profiles.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_apparmor_parser.8>.

- Load a profile into the kernel:

`sudo apparmor_parser -a {{profile_file}}`

- Replace an existing profile:

`sudo apparmor_parser -r {{profile_file}}`

- Remove a profile from the kernel:

`sudo apparmor_parser -R {{profile_name}}`

- Display help information:

`apparmor_parser --help`
