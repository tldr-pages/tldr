# sprio

> View the factors determining a job's scheduling priority.
> More information: <https://slurm.schedmd.com/sprio.html>.

- View the factors determining the scheduling priority of all jobs:

`sprio`

- View the factors determining the specified job's scheduling priority:

`sprio {{[-j|--jobs]}} {{job_id_1,job_id_2,...}}`

- Output additional information:

`sprio {{[-l|--long]}}`

- View information for the jobs of specified users:

`sprio {{[-u|--user]}} {{user_name_1,user_name_2,...}}`

- Print the weights for each factor determining job scheduling priority:

`sprio {{[-w|--weights]}}`
