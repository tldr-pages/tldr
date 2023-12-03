# sprio

> View the factors determining a job's scheduling priority
> More information: <https://slurm.schedmd.com/sprio.html>.

- View the factors determining all pending job's scheduling priority:

`sprio`

- View the factors determining the specified job's scheduling priority:

`sprio --jobs={{job_id_1,job_id_2,...}}`

- View information for the jobs of specified users and output additional information:

`sprio --user={{user_name_1,user_name_2,...}} --long`

- Print the weights for each factor determining job scheduling priority:

`sprio --weights`
