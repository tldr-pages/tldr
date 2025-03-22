# renice

> Alter the scheduling priority/niceness of running processes.
> Niceness values range from -20 (most favorable to the process) to 19 (least favorable to the process).
> See also: `nice`.
> More information: <https://manned.org/renice>.

- Set the absolute priority of a running process:

`renice --priority {{3}} {{[-p|--pid]}} {{pid}}`

- Increase the priority of a running process:

`sudo renice --relative {{-4}} {{[-p|--pid]}} {{pid}}`

- Decrease the priority of all processes owned by a user:

`renice --relative {{4}} {{[-u|--user]}} {{uid|user}}`

- Set the priority of all processes that belong to a process group:

`sudo renice {{-5}} {{[-g|--pgrp]}} {{process_group}}`
