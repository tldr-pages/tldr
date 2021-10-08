# cgcreate

> Create cgroups, used to limite, mesure, and control resources used by processes.
> You can create cgroups with types like `memory`, `cpu`, `net_cls`, etc.
> More information: <https://www.kernel.org/doc/Documentation/cgroup-v1/>.

- To install use:

`apt install cgroup-lite cgroup-tools`

- Create a new group:

`cgcreate -g {{group_type}}:{{group_name}}`

- Create a new group with multiple cgroup types:

`cgcreate -g {{group_type1}},{{group_type2}}:{{group_name}}`

- Create a subgroup:

`mkdir /sys/fs/cgroup/{{group_type}}/{{group_name}}/{{subgroup_name}}`
