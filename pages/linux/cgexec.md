# cgexec

> Use cgroups to limit, mesure, and control resources used by processes.
> cgroups has cgroup types (aka controllers) like `cpu`, `memory`, etc.
> More info: https://www.kernel.org/doc/Documentation/cgroup-v1/

- To execute a process in a given cgroup with given controller:

`cgexec -g {{controller}}:{{cgroupName}} processName`
