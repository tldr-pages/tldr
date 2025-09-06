# cgcreate

> Maak cgroups, gebruikt om bronnen te beperken, te meten en te regelen die door processen worden gebruikt.
> `cgroups` types kunnen een van `memory`, `cpu`, `net_cls`, etc. zijn.
> Meer informatie: <https://manned.org/cgcreate>.

- Maak een nieuwe groep:

`cgcreate -g {{groep_type}}:{{groepsnaam}}`

- Maak een nieuwe groep met meerdere cgroep typen:

`cgcreate -g {{groep_type1}},{{groep_type2}}:{{groepsnaam}}`

- Maak een subgroep:

`mkdir /sys/fs/cgroup/{{groep_type}}/{{groepsnaam}}/{{subgroep_naam}}`
