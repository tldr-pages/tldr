# progress

> Progress Viewer displays/monitors the progress of running coreutils.
> More information: <https://github.com/Xfennec/progress>.

- Show the progress of running coreutils once:

`progress`

- Continuously monitor the progress of running and upcoming coreutils:

`watch progress -q`

- Launch and monitor a single long-running command:

`{{command}} & progress -mp $!`
