# cpufreq-aperf

> A CPU átlagos frekvenciájának kiszámítása egy adott időszak alatt. Root-jogosultságot igényel. További információ: <https://manned.org/cpufreq-aperf>.

- Számítás megkezdése, alapértelmezés szerint minden CPU-mag és 1 másodperces frissítési időköz:

`sudo cpufreq-aperf`

- Csak az 1. CPU esetében indítsa el a számítást:

`sudo cpufreq-aperf -c {{1}}`

- Számítás indítása 3 másodperces frissítési időközzel az összes CPU-mag számára:

`sudo cpufreq-aperf -i {{3}}`

- Csak egyszeri számítás:

`sudo cpufreq-aperf -o`
