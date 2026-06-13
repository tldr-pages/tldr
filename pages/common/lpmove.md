# lpmove

> Move a job or all jobs to another printer.
> See also: `cancel`, `lp`, `lpr`, `lprm`.
> More information: <https://openprinting.github.io/cups/doc/man-lpmove.html>.

- Move a specific job to `new_printer`:

`lpmove {{job_id}} {{new_printer}}`

- Move a job from `old_printer` to `new_printer`:

`lpmove {{old_printer}}-{{job_id}} {{new_printer}}`

- Move all jobs from `old_printer` to `new_printer`:

`lpmove {{old_printer}} {{new_printer}}`

- Move a specific job to `new_printer` on a specific server:

`lpmove -h {{server}} {{job_id}} {{new_printer}}`
