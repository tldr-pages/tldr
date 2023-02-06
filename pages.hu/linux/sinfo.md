# sinfo

> A Slurm csomópontokra és partíciókra vonatkozó információk megtekintése. Lásd még: `squeue` és `sbatch`, amelyek szintén a Slurm munkaterhelés-kezelő részét képezik. További információ: <https://slurm.schedmd.com/sinfo.html>.

- A fürt gyors összefoglaló áttekintésének megjelenítése:

`sinfo --summarize`

- A teljes fürt összes partíciójának részletes állapotának megtekintése:

`sinfo`

- Egy adott partíció részletes állapotának megtekintése:

`sinfo --partition {{partition_name}}`

- Az üres csomópontokra vonatkozó információk megtekintése:

`sinfo --states {{idle}}`

- Összefoglaló a holt csomópontokról:

`sinfo --dead`

- A halott csomópontok és azok okainak felsorolása:

`sinfo --list-reasons`
