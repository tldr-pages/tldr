# jhsdb

> Attach to a Java process or launch a postmortem debugger to analyze the core dump from a crashed Java Virtual Machine.
> More information: <https://manned.org/jhsdb>.

- Print stack and locks information of a Java process:

`jhsdb jstack --pid {{pid}}`

- Open a core dump in interactive debug mode:

`jhsdb clhsdb --core {{path/to/core_dump}} --exe {{path/to/jdk/bin/java}}`

- Start a remote debug server:

`jhsdb debugd --pid {{pid}} --serverid {{optional_unique_id}}`

- Connect to a process in interactive debug mode:

`jhsdb clhsdb --pid {{pid}}`
