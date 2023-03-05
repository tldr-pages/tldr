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

- Set [p]roperties (e.g. CPUQuota, MemoryMax) of the process and wait until it exits:

`systemd-run -p MemoryMax={{memory_in_bytes}} -p CPUQuota={{percentage_of_CPU_time}}% --wait {{executable}}`

- Use the program in a shell [P]ipeline:

`{{executable1}} | systemd-run -P {{executable2}} | {{executable3}}`
