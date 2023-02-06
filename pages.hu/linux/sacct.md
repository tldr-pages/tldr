# sacct

> A Slurm szolgáltatás számviteli adatainak megjelenítése. További információ: <https://slurm.schedmd.com/sacct.html>.

- A legutóbbi munkákhoz tartozó munkaazonosító, munkanév, partíció, fiók, kiosztott processzorok száma, munkaállapot és munkakivonási kódok megjelenítése:

`sacct`

- A legutóbbi munkák munkaazonosítójának, munkaállapotának és kilépési kódjának megjelenítése:

`sacct --brief`

- Egy munka allokációinak megjelenítése:

`sacct --jobs {{job_id}} --allocations`

- A munka eltelt idejének, a munka nevének, a kért CPU-k számának és a kért memóriának a megjelenítése:

`sacct --jobs {{job_id}} --format={{elapsed}},{{jobname}},{{reqcpus}},{{reqmem}}`
