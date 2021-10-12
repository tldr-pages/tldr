# cgexec

> Limit, measure, and control resources used by processes.
> Multiple cgroup types (aka controllers) exist, such as `cpu`, `memory`, etc.
> More information: <https://manned.org/cgexec>.

- Execute a process in a given cgroup with given controller:

`cgexec -g {{controller}}:{{cgroup_name}} {{process_name}}`
