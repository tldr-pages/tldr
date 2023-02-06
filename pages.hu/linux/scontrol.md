# scontrol

> Munkahelyekkel kapcsolatos információk megtekintése és módosítása. További információ: <https://slurm.schedmd.com/scontrol.html>.

- A munkához tartozó információk megjelenítése:

`scontrol show job {{job_id}}`

- Folyamatban lévő munkák vesszővel elválasztott listájának felfüggesztése:

`scontrol suspend {{job_id}}`

- A felfüggesztett munkák vesszővel elválasztott listájának folytatása:

`scontrol resume {{job_id}}`

- Sorba állított munkák vesszővel elválasztott listájának tartása (a `release` paranccsal engedélyezheti a munkák ütemezését):

`scontrol hold {{job_id}}`

- Felfüggesztett munkák vesszővel elválasztott listájának feloldása:

`scontrol release {{job_id}}`
