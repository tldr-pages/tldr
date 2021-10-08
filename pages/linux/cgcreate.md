# cgcreate

> Create cgroups, used to limite, mesure, and control resources used by processes.
> You can create cgroups with types like `memory`, `cpu`, `net_cls`, etc.
> More information: <https://www.kernel.org/doc/Documentation/cgroup-v1/>.

- To install use:

`apt install cgroup-lite cgroup-tools`

- Create a new group:

`cgcreate -g {{group_type}}:{{group_name}}`

- To create a new group with multiple croup types:

`cgcreate -g {{groupType1}},{{groupType2}}:{{groupName}}`

- To create subgroups:

`mkdir /sys/fs/cgroup/{{groupType}}/{{groupName}}/{{subgroupName}}`
