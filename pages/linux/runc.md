# runc

> Run applications packaged according to the Open Container Initiative (OCI) format.
> Note: Rootless containers can store their state in a custom directory with `--root {{path/to/state_dir}}`.
> See also: `ctr`, `nerdctl`.
> More information: <https://manpages.debian.org/latest/runc/runc.8.html>.

- Generate a default OCI bundle specification (`config.json`) in the current directory:

`runc spec`

- Create and start a container from the bundle in the current directory:

`sudo runc run {{container_id}}`

- Create a container from a specific bundle without starting it:

`sudo runc create --bundle {{path/to/bundle}} {{container_id}}`

- Start a previously created container:

`sudo runc start {{container_id}}`

- Run a command inside a running container:

`sudo runc exec {{[-t|--tty]}} {{container_id}} {{command}}`

- List containers created by `runc`:

`sudo runc list`

- Send a `KILL` signal to a container:

`sudo runc kill {{container_id}} KILL`

- Forcefully remove a container:

`sudo runc delete --force {{container_id}}`
