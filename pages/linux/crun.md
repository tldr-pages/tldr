# crun

> Fast and lightweight runtime for running OCI containers.
> More information: <https://manned.org/crun>.

- Generate a default OCI configuration file (`config.json`):

`crun spec`

- Generate an OCI configuration file for rootless containers:

`crun spec --rootless`

- Create and run a container from a bundle directory:

`crun run --bundle {{path/to/bundle}} {{container_id}}`

- Start a previously created container:

`crun start {{container_id}}`

- List running containers:

`crun list`

- Execute a command inside a running container:

`crun exec {{container_id}} {{command}}`

- Send a signal to a container's init process:

`crun kill {{container_id}} {{signal_name}}`

- Delete a stopped container:

`crun delete {{container_id}}`
