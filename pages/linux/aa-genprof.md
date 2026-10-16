# aa-genprof

> Generate AppArmor security profiles by monitoring program behavior.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-genprof.8>.

- Start generating a profile for a program:

`sudo aa-genprof {{path/to/program}}`

- Specify a custom directory for profiles:

`sudo aa-genprof {{[-d|--dir]}} /{{path/to/profiles}} {{path/to/program}}`

- Specify a custom logfile for profiling:

`sudo aa-genprof {{[-f|--file]}} /{{path/to/logfile}} {{path/to/program}}`

- Display help:

`aa-genprof {{[-h|--help]}}`
