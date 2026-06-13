# resticprofile schedule

> Schedule backups and run them in the background.
> See also: `restic`, `resticprofile`, `resticprofile-unschedule`.
> More information: <https://creativeprojects.github.io/resticprofile/schedules/configuration/index.html>.

- Schedule default profile:

`resticprofile schedule`

- Schedule a profile (default profile is "default"):

`resticprofile --name "{{group_name}}" schedule`

- Schedule all profiles:

`resticprofile schedule --all`

- Don't start the job after installing:

`resticprofile schedule --no-start`

- Display status of scheduled jobs for a profile:

`resticprofile status {{[-n|--name]}} {{profile_name}}`

- Run a scheduled job manually (used by system scheduler):

`resticprofile run-schedule "backup@{{profile_name}}"`
