# cpufreq-set

> A CPU frekvencia beállításainak módosítására szolgáló eszköz. A frekvenciaértéknek a `cpufreq-info -l` parancs kimenete között kell lennie. További információ: <https://manned.org/cpufreq-set>.

- Állítsa a CPU 1 CPU frekvenciapolitikáját "userspace" értékre:

`sudo cpufreq-set -c {{1}} -g {{userspace}}`

- A CPU 1 aktuális minimális CPU-frekvenciájának beállítása:

`sudo cpufreq-set -c {{1}} --min {{min_frequency}}`

- A CPU 1 jelenlegi maximális CPU-frekvenciájának beállítása:

`sudo cpufreq-set -c {{1}} --max {{max_frequency}}`

- A CPU 1 aktuális munkafrekvenciájának beállítása:

`sudo cpufreq-set -c {{1}} -f {{work_frequency}}`
