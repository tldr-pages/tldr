# cgclassify

> Move running tasks to `cgroups`.
> More information: <https://manned.org/cgclassify>.

- Move the process with a specific PID to the control group student in the CPU hierarchy:

`cgclassify -g {{cpu:student}} {{1234}}`

- Move the process with a specific PID to control groups based on the `/etc/cgrules.conf` configuration file:

`cgclassify {{1234}}`

- Move the process with a specific PID to the control group student in the CPU hierarchy. Note: The daemon of the service `cgred` does not change `cgroups` of the specific PID and its children (based on `/etc/cgrules.conf`):

`cgclassify --sticky -g {{cpu:/student}} {{1234}}`
