# sattach

> Attach to a `Slurm` job step.
> More information: <https://manned.org/sattach>.

- Attach to a specific job step:

`sattach {{job}}.{{step}}`

- Display up to a specific task, job and step:

`sattach --output-filter {{task}} {{job}}.{{step}}`
