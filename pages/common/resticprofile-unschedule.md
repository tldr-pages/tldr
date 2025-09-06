# resticprofile unschedule

> The command removes jobs for schedules declared in the selected profile or group (or of all profiles and groups).
> See also: `restic`, `resticprofile`, `resticprofile-schedule`.
> More information: <https://creativeprojects.github.io/resticprofile/schedules/configuration/index.html>.

- Unschedule a backup for a specific profile:

`resticprofile unschedule {{[-n|--name]}} "{{profile_name}}"`

- Unschedule all backups:

`resticprofile unschedule --all`
