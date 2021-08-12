# sacctmgr

> Vizualizați, configurați și gestionați conturile Slurm.
> Mai multe informaţii: <https://slurm.schedmd.com/sacctmgr.html>

- Afișează configurația curentă:

`sacctmgr show configuration`

- Adăugați un cluster la baza de date slurm:

`sacctmgr add cluster {{cluster_name}}`

- Adaugă un cont la baza de date slurm:

`sacctmgr add account {{account_name}} cluster={{cluster_of_account}}`

- Afișează detaliile utilizatorului/asociației/clusterului/contului:

`sacctmgr show {{user/association/cluster/account}}`
