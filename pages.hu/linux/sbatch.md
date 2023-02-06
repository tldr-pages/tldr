# sbatch

> Kötegelt feladat elküldése a SLURM ütemezőnek. További információ: <https://manned.org/sbatch>.

- Kötegelt feladat elküldése:

`sbatch {{path/to/job.sh}}`

- Egyéni névvel ellátott kötegelt feladat elküldése:

`sbatch --job-name={{myjob}} {{path/to/job.sh}}`

- Kötegelt feladat elküldése 30 perces időkorlátozással:

`sbatch --time={{00:30:00}} {{path/to/job.sh}}`

- Feladat elküldése és több csomópont igénylése:

`sbatch --nodes={{3}} {{path/to/job.sh}}`
