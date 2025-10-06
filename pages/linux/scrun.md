# scrun

> An OCI runtime proxy for Slurm that runs containers as jobs.
> More information: <https://slurm.schedmd.com/scrun.html>.

- Create a new container with a specific ID:

`scrun create {{container_id}}`

- Start a previously created container:

`scrun start {{container_id}}`

- Query the state of a container:

`scrun state {{container_id}}`

- Send a signal to a container (default: SIGTERM):

`scrun kill {{container_id}}`

- Send a specific signal to a container:

`scrun kill {{container_id}} {{SIGKILL}}`

- Delete a container and release its resources:

`scrun delete {{container_id}}`

- Enable debug logging:

`scrun {{create|start|kill|delete}} {{container_id}} --debug`

- Display version:

`scrun --version`
