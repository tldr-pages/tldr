# nomad

> Distributed, highly available, datacenter-aware scheduler.
> More information: <https://www.nomadproject.io/docs/commands/>.

- Show the status of nodes in the cluster:

`nomad node status`

- Validate a job file:

`nomad job validate {{path/to/file.nomad}}`

- Plan a job for execution on the cluster:

`nomad job plan {{path/to/file.nomad}}`

- Run a job on the cluster:

`nomad job run {{path/to/file.nomad}}`

- Show the status of jobs currently running on the cluster:

`nomad job status`

- Show the detailed status information about a specific job:

`nomad job status {{job_name}}`

- Follow the logs of a specific allocation:

`nomad alloc logs {{alloc_id}}`

- Show the status of storage volumes:

`nomad volume status`
