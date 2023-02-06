# cgexec

> A folyamatok által használt erőforrások korlátozása, mérése és ellenőrzése. Többféle cgroup típus (más néven vezérlő) létezik, például `cpu`, `memory`, stb. További információ: <https://manned.org/cgexec>.

- Egy adott cgroupban lévő folyamat végrehajtása adott vezérlővel:

`cgexec -g {{controller}}:{{cgroup_name}} {{process_name}}`
