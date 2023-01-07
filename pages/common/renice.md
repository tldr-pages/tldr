# renice

> Alters the scheduling priority/niceness of one or more running processes.
> Niceness values range from -20 (most favorable to the process) to 19 (least favorable to the process).
> More information: <https://manned.org/renice>.

- Change priority of a running process:

`renice -n {{niceness_value}} -p {{pid}}`

- Change priority of all processes owned by a user:

`renice -n {{niceness_value}} -u {{user}}`

- Change priority of all processes that belong to a process group:

`renice -n {{niceness_value}} --pgrp {{process_group}}`
