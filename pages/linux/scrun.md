# scrun

> An OCI (Open Container Initiative) runtime proxy for Slurm.
> More information: <https://slurm.schedmd.com/scrun.html>.

- Create a container in the current directory:

`scrun create {{container_id}}`

- Start a container in a Slurm job:

`scrun start {{container_id}}`

- View the state of the specified container:

`scrun state {{container_id}}`

- Send the specified signal to a container:

`scrun kill {{container_id}} {{SIGTERM}}`

- Delete the specified container:

`scrun delete {{container_id}}`
