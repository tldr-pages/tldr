# sstat

> A futó munkákkal kapcsolatos információk megtekintése. További információ: <https://slurm.schedmd.com/sstat.html>.

- Munkák vesszővel elválasztott listájának állapotinformációinak megjelenítése:

`sstat --jobs={{job_id}}`

- A munkák vesszővel elválasztott listájának munkák azonosítójának, átlagos CPU-jának és átlagos virtuális memóriaméretének megjelenítése, oszlophatárolóként pipákkal:

`sstat --parsable --jobs={{job_id}} --format={{JobID}},{{AveCPU}},{{AveVMSize}}`

- Az elérhető mezők listájának megjelenítése:

`sstat --helpformat`
