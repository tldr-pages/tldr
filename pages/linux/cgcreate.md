# cgcreate

> Create cgroups, used to limit, measure, and control resources used by processes.
> `cgroups` types can be `memory`, `cpu`, `net_cls`, etc.
> More information: <https://manned.org/cgcreate>.

- Create a new group:

`cgcreate -g {{group_type}}:{{group_name}}`

- Create a new group with multiple cgroup types:

`cgcreate -g {{group_type1}},{{group_type2}}:{{group_name}}`

- Create a subgroup:

`mkdir /sys/fs/cgroup/{{group_type}}/{{group_name}}/{{subgroup_name}}`
