# jhsdb

> Attach to a Java process or launch a postmortem debugger to analyze the core dump from a crashed Java Virtual Machine.
> More information: <https://manned.org/jhsdb>.

- Use a PID to connect to a hung process:

`jhsdb jstack --pid {{pid}}`

- Open a core dump for analysis:

`jhsdb clhsdb --core {{path/to/core_dump}} --exe {{/path/to/jdk/bin/java}}`

- Start a debug server:

`jhsdb debugd --pid {{pid}} --serverid {{optional_unique_id}}`

- Connect to process in clhsdb mode:

`jhsdb clhsdb --pid {{pid}}`
