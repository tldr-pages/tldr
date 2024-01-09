# renice

> Alter the scheduling priority/niceness of one or more running processes.
> Niceness values range from -20 (most favorable to the process) to 19 (least favorable to the process).
> See also: `nice`.
> More information: <https://manned.org/renice>.

- Set the absolute priority of a running [p]rocess:

`renice {{+3}} -p {{pid}}`

- Increase/decrease the priority of all processes owned by a [u]ser:

`renice --relative {{-4}} -u {{uid|user}}`

- Set the priority of all processes that belong to a process [g]roup:

`renice --absolute {{5}} -g {{process_group}}`
