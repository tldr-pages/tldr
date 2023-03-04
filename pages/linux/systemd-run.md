# systemd-run

> Run programs in transient scope units, service units, or path-, socket-, or timer-triggered service units.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-run.html>.

- Run a program as root:

`systemd-run {{executable}}`

- Run a program in the user service, keeping the working [d]irectory and waiting until it exits:

`systemd-run --user -d {{executable}}`

- Provide a custom [u]nit name and pass extra parameters:

`systemd-run -u {{unit_name}} -- {{executable}} {{extra parameters ...}}`

- Share the [t]erminal with the program (allowing interactive input/output) and make sure the execution details [r]emain after the program exits:

`systemd-run -rt {{executable}}`

- Limit the CPU and memory utilization of the process, set other [p]roperties and wait until it exits:

`systemd-run -p MemoryMax={{memory_in_bytes}} -p CPUQuota={{percentage_of_CPU_time}}% -p {{other_property=value}} --wait {{executable}}`

- Use the program in a shell [P]ipeline:

`{{other_executable}} | systemd-run -P {{executable}} | {{other_executable}}`
