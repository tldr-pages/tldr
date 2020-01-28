# progress

> Display/Monitor the progress of running coreutils.
> More information: <https://github.com/Xfennec/progress>.

- Show the progress of running coreutils:

`progress`

- Show the progress of running coreutils with minimized output:

`progress -q`

- Launch and monitor a single long-running command:

`{{command}} & progress -mp $!`
