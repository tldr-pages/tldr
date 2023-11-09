# cgclassify

> Move running task(s) to given `cgroups`.
> More information: <https://manned.org/cgclassify>.

- Move process with pid number 1234 to control group student in cpu hierarchy:

`cgclassify -g {{cpu:student}} {{1234}}`

- Move process with pid number 1234 to control groups based on `/etc/cgrules.conf` configuration file:

`cgclassify {{1234}}`

- Move process with pid number 1234 to control group student in cpu hierarchy. The daemon of service `cgred` does not change cgroups of pid 1234 and its children (based on `/etc/cgrules.conf`):

`cgclassify --sticky -g {{cpu:/student}} {{1234}}`
