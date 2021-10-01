# jhsdb

> Attach to a Java process or launch a postmortem debugger to analyze the content of a core dump from a crashed Java Virtual Machine (JVM).

- Using pid to connect to a hung process:

`jhsdb jstack --pid {{pid}}`

- Open a core dump for analysis:

`jhsdb clhsdb --core {{./core}} --exe {{/path/to/jdk/bin/java}}`

- Start a debug server:

`jhsdb debugd --pid {{pid}} --serverid {{server_id}}`

- Connect to process in clhsdb mode:

`jhsdb clhsdb --pid {{pid}}`
