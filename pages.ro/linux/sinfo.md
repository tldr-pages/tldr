# sinfo

> Vizualizați informații despre nodurile și partițiile Slurm.
> A se vedea, de asemenea, `squeue` și `sbatch`, care fac parte, de asemenea, din managerul volumului de lucru Slurm.
> Mai multe informaţii: <https://slurm.schedmd.com/sinfo.html>

- Afișează o prezentare generală rapidă a clusterului:

`sinfo --summarize`

- Vizualizați starea detaliată a tuturor partițiilor din întregul cluster:

`sinfo`

- Vizualizați starea detaliată a unei anumite partiții:

`sinfo --partition {{partition_name}}`

- Vezi informații despre nodurile inactive:

`sinfo --states {{idle}}`

- Rezumăm nodurile moarte:

`sinfo --dead`

- Lista nodurilor moarte și motivele pentru care:

`sinfo --list-reasons`
