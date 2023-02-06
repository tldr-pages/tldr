# squeue

> A SLURM ütemezőben sorba állított feladatok megtekintése. További információ: <https://manned.org/squeue>.

- A várólista megtekintése:

`squeue`

- Egy adott felhasználó által sorba állított munkák megtekintése:

`squeue -u {{username}}`

- A várólista megtekintése és 5 másodpercenkénti frissítése:

`squeue -i {{5}}`

- A várólista megtekintése a várható kezdési időpontokkal:

`squeue --start`
