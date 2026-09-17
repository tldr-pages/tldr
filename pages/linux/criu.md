# criu

> Freeze a running application or a process tree and restore it later.
> More information: <https://manned.org/criu>.

- Check if the current kernel has support for the necessary CRIU features:

`sudo criu check`

- Checkpoint a process with a specific ID, saving the state to a specific directory:

`sudo criu dump {{[-t|--tree]}} {{process_id}} {{[-D|--images-dir]}} {{path/to/directory}}`

- Restore a process from previously saved image files:

`sudo criu restore {{[-D|--images-dir]}} {{path/to/directory}}`

- Dump a process and allow it to continue running instead of terminating it:

`sudo criu dump {{[-t|--tree]}} {{process_id}} {{[-D|--images-dir]}} {{path/to/directory}} {{[-R|--leave-running]}}`
