# strigger

> View or modify Slurm trigger information.
> Triggers are actions that are automatically run when an event occurs on a Slurm cluster.
> More information: <https://slurm.schedmd.com/strigger.html>.

- Register a new trigger. Execute the specified program when the specified event occurs:

`strigger --set --{{primary_database_failure|primary_slurmdbd_failure|primary_slurmctld_acct_buffer_full|primary_slurmctld_failure|...}} {{[-p|--program]}} {{path/to/executable}}`

- Execute the specified program when the specified job terminated:

`strigger --set {{[-j|--jobid]}} {{job_id}} {{[-f|--fini]}} {{[-p|--program]}} "{{path/to/executable}} {{argument1 argument2 ...}}"`

- View active triggers:

`strigger --get`

- View active triggers regarding the specified job:

`strigger --get {{[-j|--jobid]}} {{job_id}}`

- Clear the specified trigger:

`strigger --clear {{trigger_id}}`
