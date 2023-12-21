# sattach

> Attach to a Slurm job step.
> More information: <https://slurm.schedmd.com/sattach.html>.

- Redirect the IO streams (`stdout`, `stderr`, and `stdin`) of a Slurm job step to the current terminal:

`sattach {{jobid}}.{{stepid}}`

- Use the current console's input as `stdin` to the specified task:

`sattach --input-filter {{task_number}}`

- Only redirect `stdin`/`stderr` of the specified task:

`sattach --{{output|error}}-filter {{task_number}}`
