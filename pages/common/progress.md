# progress

> Display/Monitor the progress of running coreutils.
> More information: <https://github.com/Xfennec/progress>.

- Show the progress of running coreutils:

`progress`

- Monitor all running coreutils:

`progress {{[-m|--monitor]}}`

- Show the progress of running coreutils in quiet mode:

`progress {{[-q|--quiet]}}`

- Launch and monitor a single long-running command:

`{{command}} & progress {{[-m|--monitor]}} {{[-p|--pid]}} $!`

- Include an estimate of time remaining for completion:

`progress {{[-w|--wait]}} {{[-c|--command]}} {{firefox}}`
