# nomad

> Elosztott, nagy rendelkezésre állású, adatközpont-tudatos ütemező. További információ: <https://www.nomadproject.io/docs/commands/>.

- A fürt csomópontjainak állapotának megjelenítése:

`nomad node status`

- Feladatfájl hitelesítése:

`nomad job validate {{path/to/file.nomad}}`

- Tervezzen meg egy feladatot a fürtön történő végrehajtáshoz:

`nomad job plan {{path/to/file.nomad}}`

- Egy feladat futtatása a fürtön:

`nomad job run {{path/to/file.nomad}}`

- A fürtön jelenleg futó feladatok állapotának megjelenítése:

`nomad job status`

- Egy adott feladat részletes állapotinformációinak megjelenítése:

`nomad job status {{job_name}}`

- Egy adott kiosztás naplóinak követése:

`nomad alloc logs {{alloc_id}}`

- A tároló kötetek állapotának megjelenítése:

`nomad volume status`
