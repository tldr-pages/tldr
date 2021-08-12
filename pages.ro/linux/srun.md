# srun

> Creați o activitate de tip slurm interactiv sau conectați-vă la o activitate existentă.
> Mai multe informaţii: <https://slurm.schedmd.com/srun.html>

- Trimite un loc de muncă interactiv de bază:

`srun --pty /bin/bash`

- Trimite un loc de muncă interactiv cu atribute diferite:

`srun --ntasks-per-node={{num_cores}} --mem-per-cpu={{memory_MB}} --pty /bin/bash`

- Conectați-vă la un nod de lucrător cu un loc de muncă care rulează:

`srun --jobid={{job_id}} --pty /bin/bash`
