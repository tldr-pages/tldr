# scontrol

> Vizualizaţi informaţii despre şi modificaţi activităţile.
> Mai multe informaţii: <https://slurm.schedmd.com/scontrol.html>

- Afișați informații pentru locuri de muncă:

`scontrol show job {{job_id}}`

- Suspendarea unei liste separate prin virgulă de locuri de muncă care rulează:

`scontrol suspend {{job_id}}`

- Reluați o listă separată prin virgulă de locuri de muncă suspendate:

`scontrol resume {{job_id}}`

- Țineți o listă separată prin virgulă de locuri de muncă în coada de așteptare (Utilizați comanda `lansare” pentru a permite programarea locurilor de muncă):

`scontrol hold {{job_id}}`

- Eliberați o listă separată prin virgulă de locuri de muncă suspendate:

`scontrol release {{job_id}}`
