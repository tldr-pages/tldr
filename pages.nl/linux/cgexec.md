# cgexec

> Beperk, meet en beheers bronnen die door processen worden gebruikt.
> Er bestaan meerdere cgroup types (oftwel controllers), zoals `cpu`, `memory`, etc.
> Meer informatie: <https://manned.org/cgexec>.

- Voer een proces uit in een bepaalde cgroup met een bepaalde controller:

`cgexec -g {{controller}}:{{cgroup_name}} {{process_name}}`
