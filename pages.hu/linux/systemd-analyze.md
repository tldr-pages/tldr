# systemd-analyze

> A rendszergazda elemzése és hibakeresése. Megjeleníti az egységek indítási folyamatának időzítési részleteit (szolgáltatások, csatolási pontok, eszközök, aljzatok). További információk: <https://manned.org/systemd-analyze>.

- Listázza az egyes egységek indulási idejét:

`systemd-analyze blame`

- Kiírja az egységek időkritikus láncának fáját:

`systemd-analyze critical-chain`

- Készítsen egy SVG-fájlt, amely megmutatja, hogy az egyes rendszerszolgáltatások mikor indultak el, kiemelve az inicializálásra fordított időt:

`systemd-analyze plot > {{path/to/file.svg}}`

- Rajzoljon függőségi grafikont, és alakítsa át SVG-fájlba:

`systemd-analyze dot | dot -T{{svg}} > {{path/to/file.svg}}`

- Mutassa meg a futó egységek biztonsági pontszámát:

`systemd-analyze security`
