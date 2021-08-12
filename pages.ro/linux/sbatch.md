# sbatch

> Trimiteți un loc de muncă lot la programatorul SLURM.

- Trimite un loc de muncă lot:

`sbatch {{path/to/job.sh}}`

- Trimiteți un loc de muncă lot cu un nume personalizat:

`sbatch --job-name={{myjob}} {{path/to/job.sh}}`

- Trimiteți un loc de muncă în serie cu o limită de timp de 30 de minute:

`sbatch --time={{00:30:00}} {{path/to/job.sh}}`

- Trimiteți un loc de muncă și solicitați mai multe noduri:

`sbatch --nodes={{3}} {{path/to/job.sh}}`
