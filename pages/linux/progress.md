# progress

> A lightweight progress monitor. It displays the progress of running coreutils. 
> More information: <https://github.com/Xfennec/progress>.

- List progress of running coreutils once:

`progress`

- Continuously monitor progress of running and upcoming coreutils:

`watch progress -q`

- Launch and monitor a single long-running command:

`{{command}} & progress -mp $!`
