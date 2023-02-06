# srun

> Interaktív slurm feladat létrehozása vagy csatlakozás egy meglévő feladathoz. További információ: <https://slurm.schedmd.com/srun.html>.

- Alapvető interaktív feladat beküldése:

`srun --pty /bin/bash`

- Interaktív feladat elküldése különböző attribútumokkal:

`srun --ntasks-per-node={{num_cores}} --mem-per-cpu={{memory_MB}} --pty /bin/bash`

- Csatlakozás egy olyan munkáscsomóponthoz, ahol már fut egy feladat:

`srun --jobid={{job_id}} --pty /bin/bash`
