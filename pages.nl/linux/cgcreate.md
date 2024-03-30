# cgcreate

> Maak cgroups, gebruikt om bronnen te beperken, te meten en te regelen die door processen worden gebruikt.
> `cgroups` types kunnen een van `memory`, `cpu`, `net_cls`, etc. zijn.
> Meer informatie: <https://manned.org/cgcreate>.

- Maak een nieuwe groep:

`cgcreate -g {{group_type}}:{{group_name}}`

- Maak een nieuwe groep met meerdere cgroep typen:

`cgcreate -g {{group_type1}},{{group_type2}}:{{group_name}}`

- Maak een subgroep:

`mkdir /sys/fs/cgroup/{{group_type}}/{{group_name}}/{{subgroup_name}}`
