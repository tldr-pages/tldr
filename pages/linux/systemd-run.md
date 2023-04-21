# systemd-run

> Run programs in transient scope units, service units, or path-, socket-, or timer-triggered service units.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-run.html>.

- Start a transient service:

`sudo systemd-run {{command}} {{argument1 argument2 ...}}`

- Start a transient service under the service manager of the current user (no privileges):

`systemd-run --user {{command}} {{argument1 argument2 ...}}`

- Start a transient service with a custom unit name and description:

`sudo systemd-run --unit={{name}} --description={{string}} {{command}} {{argument1 argument2 ...}}`

- Start a transient service that does not get cleaned up after it terminates with a custom environment variable:

`sudo systemd-run --remain-after-exit --set-env={{name}}={{value}} {{command}} {{argument1 argument2 ...}}`

- Start a transient timer that periodically runs its transient service (see `man systemd.time` for calendar event format):

`sudo systemd-run --on-calendar={{calendar_event}} {{command}} {{argument1 argument2 ...}}`

- Share the terminal with the program (allowing interactive input/output) and make sure the execution details remain after the program exits:

`systemd-run  --remain-after-exit --pty {{executable}}`

- Set properties (e.g. CPUQuota, MemoryMax) of the process and wait until it exits:

`systemd-run --property MemoryMax={{memory_in_bytes}} --property CPUQuota={{percentage_of_CPU_time}}% --wait {{executable}}`

- Use the program in a shell pipeline:

`{{executable1}} | systemd-run --pipe {{executable2}} | {{executable3}}`
