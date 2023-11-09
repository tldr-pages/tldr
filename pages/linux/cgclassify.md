# cgclassify

> Move running task(s) to given `cgroups`.
> More information: <https://manned.org/cgclassify>.

- Move the process with PID 1234 to control group student in the CPU hierarchy:

`cgclassify -g {{cpu:student}} {{1234}}`

- Move the process with PID 1234 to control groups based on the `/etc/cgrules.conf` configuration file:

`cgclassify {{1234}}`

- Move the process with PID 1234 to the control group student in the CPU hierarchy. The daemon of the service `cgred` does not change cgroups of PID 1234 and its children (based on `/etc/cgrules.conf`):

`cgclassify --sticky -g {{cpu:/student}} {{1234}}`
