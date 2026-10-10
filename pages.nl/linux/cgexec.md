# cgexec

> Beperk, meet en beheers bronnen die door processen worden gebruikt.
> Er bestaan meerdere cgroup types (oftewel controllers), zoals `cpu`, `memory`, etc.
> Meer informatie: <https://manned.org/cgexec>.

- Voer een proces uit in een bepaalde c[g]roup met een bepaalde controller:

`cgexec -g {{controller}}:{{cgroup_naam}} {{proces_naam}}`
