# bsub

> Submit batch jobs to LSF (Load Sharing Facility) scheduler.
> More information: <https://www.ibm.com/docs/spectrum-lsf/latest?topic=reference-bsub>.

- Submit a script file as a job:

`bsub {{path/to/script.sh}}`

- Submit a job to a specific queue:

`bsub -q {{queue_name}} make all`

- Submit a job with a name and redirect output and error:

`bsub -J {{job_name}} --output {{path/to/output.log}} --error {{path/to/error.log}} {{path/to/script.sh}}`

- Request 8 CPU cores and 16GB memory for a command:

`bsub -n 8 -M 16G cargo build --release`

- Run an interactive shell in the current session:

`bsub -I bash`

- Submit a job with a runtime limit of 45 minutes:

`bsub -W 45 {{path/to/script.sh}}`
