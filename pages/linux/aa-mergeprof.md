# aa-mergeprof

> Merge AppArmor security profiles from multiple sources.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-mergeprof.8>.

- Merge profiles from a directory into the current profile:

`sudo aa-mergeprof {{/path/to/profiles}}`

- Merge profiles and overwrite existing rules:

`sudo aa-mergeprof --force {{/path/to/profiles}}`

- Display help information:

`aa-mergeprof --help`
