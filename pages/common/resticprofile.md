# resticprofile

> Configuration profiles manager for restic backup.
> See also: `restic`, `resticprofile-schedule`, `resticprofile-unschedule`.
> More information: <https://creativeprojects.github.io/resticprofile/configuration/getting_started/index.html#write-your-first-configuration-file>.

- List all saved snapshots:

`resticprofile`

- Run a backup on the default profile:

`resticprofile backup`

- Run a backup with a specific profile (default profile is "default"):

`resticprofile {{[-n|--name]}} "{{profile_name}}" backup`

- Run in dry-run mode and show the underlying restic commands:

`resticprofile --dry-run backup`

- Display the names of all profiles from the configuration file:

`resticprofile profiles`

- Generate shell completions:

`resticprofile generate {{--bash-completion|--zsh-completion}}`

- Show all details of a profile:

`resticprofile show {{[-n|--name]}} "{{profile_name}}"`
