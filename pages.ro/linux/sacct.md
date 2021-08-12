# sacct

> Afișați datele contabile din serviciul Slurm.
> Mai multe informaţii: <https://slurm.schedmd.com/sacct.html>

- Afișați ID-ul postului, numele postului, partiția, contul, numărul de procesoare alocate, starea postului și codurile de ieșire de locuri de muncă pentru locuri de muncă recente:

`sacct`

- Afișează ID-ul postului, starea postului, codul de ieșire de locuri de muncă pentru locurile de muncă recente:

`sacct --brief`

- Afișează alocările unui loc de muncă:

`sacct --jobs {{job_id}} --allocations`

- Afișarea timpului scurs, numele postului, numărul procesoarelor solicitate și memoria solicitată de un loc de muncă:

`sacct --jobs {{job_id}} --format={{elapsed}},{{jobname}},{{reqcpus}},{{reqmem}}`
