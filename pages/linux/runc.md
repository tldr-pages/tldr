# runc

> CLI tool for spawning and running containers according to the OCI specification.
> More information: <https://github.com/opencontainers/runc>.

- Generate a default OCI configuration file (`config.json`):

`runc spec`

- Generate an OCI configuration file for rootless containers:

`runc spec --rootless`

- Create and run a container from a bundle directory:

`runc run --bundle {{path/to/bundle}} {{container_id}}`

- Start a previously created container:

`runc start {{container_id}}`

- List containers:

`runc list`

- Execute a command inside a running container:

`runc exec {{container_id}} {{command}}`

- Send a signal to a container's init process:

`runc kill {{container_id}} {{signal_name}}`

- Delete a stopped container:

`runc delete {{container_id}}`
