# criu

> Checkpoint/Restore In Userspace.
> Freeze a running application or a process tree and restore it later.
> More information: <https://criu.org>.

- Checkpoint a process with a specific ID (PID), saving the state to the current directory:
`criu dump -t {{pid}} --images-dir {{path/to/directory}}`

- Restore a process from previously saved image files:
`criu restore --images-dir {{path/to/directory}}`

- Check if the current kernel has support for the necessary CRIU features:
`criu check`

- Dump a process and allow it to continue running instead of terminating it:
`criu dump -t {{pid}} --images-dir {{path/to/directory}} --leave-running`
