# renice

> Alter the scheduling priority/niceness of running processes. Niceness values range from -20 (most favorable to the process) to 19 (least favorable to the process).
> See also: `nice`.
> More information: <https://manned.org/renice.1p>.

- Increase/decrease the priority of a running process:

`renice -n {{3}} -p {{process_id}}`

- Increase/decrease the priority of all processes owned by a user:

`renice -n {{-4}} -u {{user_id}}`

- Increase/decrease the priority of all processes that belong to a process group:

`renice -n {{5}} -g {{process_group}}`
