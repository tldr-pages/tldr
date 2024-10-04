# cgcreate

> Cria cgroups, usados para limitar, medir e controlar recursos usados pelos processos.
> Tipos de `cgroups` podem ser `memory`, `cpu`, `net_cls`, etc.
> Mais informações: <https://manned.org/cgcreate>.

- Cria um novo grupo:

`cgcreate -g {{tipo_grupo}}:{{nome_grupo}}`

- Cria um novo grupo com vários tipos de cgroup:

`cgcreate -g {{tipo_grupo1}},{{tipo_grupo2}}:{{nome_grupo}}`

- Cria um subgrupo:

`mkdir /sys/fs/cgroup/{{tipo_grupo2}}/{{nome_grupo}}/{{nome_subgrupo}}`
