# sacctmgr

> Slurm-fiókok megtekintése, beállítása és kezelése. További információ: <https://slurm.schedmd.com/sacctmgr.html>.

- Jelenlegi konfiguráció megjelenítése:

`sacctmgr show configuration`

- Fürt hozzáadása a slurm adatbázisához:

`sacctmgr add cluster {{cluster_name}}`

- Fiók hozzáadása a slurm adatbázishoz:

`sacctmgr add account {{account_name}} cluster={{cluster_of_account}}`

- A felhasználó/társulás/klaszter/számla adatainak megjelenítése meghatározott formátumban:

`sacctmgr show {{user|association|cluster|account}} format="Account%10" format="GrpTRES%30"`
