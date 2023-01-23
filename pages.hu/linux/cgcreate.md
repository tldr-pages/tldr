# cgcreate

> A folyamatok által használt erőforrások korlátozására, mérésére és ellenőrzésére használt cgroups létrehozása.`cgroups` típusok lehetnek: `memory`, `cpu`, `net_cls`, stb. További információ: <https://manned.org/cgcreate>.

- Új csoport létrehozása:

`cgcreate -g {{group_type}}:{{group_name}}`

- Új csoport létrehozása több cgroup típussal:

`cgcreate -g {{group_type1}},{{group_type2}}:{{group_name}}`

- Alcsoport létrehozása:

`mkdir /sys/fs/cgroup/{{group_type}}/{{group_name}}/{{subgroup_name}}`
