# apparmor_parser

> Load, compile, and manage AppArmor security profiles.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_apparmor_parser.8>.

- Load a profile into the kernel:

`sudo apparmor_parser {{[-a|--add]}} {{profile_file}}`

- Replace an existing profile:

`sudo apparmor_parser {{[-r|--replace]}} {{profile_file}}`

- Remove a profile from the kernel:

`sudo apparmor_parser {{[-R|--remove]}} {{profile_name}}`

- Load a profile in complain mode (logs violations but doesn't block):

`sudo apparmor_parser {{[-C|--complain]}} {{[-r|--replace]}} {{path/to/profile}}`

- Preprocess a profile (resolve includes) and write binary cache to file:

`apparmor_parser {{[-p|--preprocess]}} {{[-o|--ofile]}} {{path/to/output.cache}} {{[-Q|--skip-kernel-load]}} {{path/to/profile}}`

- Preprocess and print binary profile to stdout without loading:

`apparmor_parser {{[-p|--preprocess]}} {{[-S|--stdout]}} {{[-Q|--skip-kernel-load]}} {{path/to/profile}}`

- Replace a profile while skipping cache reads:

`sudo apparmor_parser {{[-r|--replace]}} {{[-T|--skip-read-cache]}} {{path/to/profile}}`

- Replace a profile, rebuild cache, and write it to a custom directory:

`sudo apparmor_parser {{[-r|--replace]}} {{[-W|--write-cache]}} {{[-L|--cache-loc]}} {{/path/to/cache}} {{path/to/profile}}`
