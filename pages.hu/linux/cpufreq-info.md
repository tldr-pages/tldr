# cpufreq-info

> A CPU frekvencia információk megjelenítésére szolgáló eszköz. További információ: <https://manned.org/cpufreq-info>.

- CPU-frekvencia információk megjelenítése az összes CPU számára:

`cpufreq-info`

- A megadott CPU CPU frekvenciainformációinak megjelenítése:

`cpufreq-info -c {{cpu_number}}`

- A megengedett minimális és maximális CPU-frekvencia megjelenítése:

`cpufreq-info -l`

- Az aktuális minimális és maximális CPU-frekvencia és házirend megjelenítése táblázatos formában:

`cpufreq-info -o`

- Elérhető CPU-frekvencia házirendek megjelenítése:

`cpufreq-info -g`

- Az aktuális CPU-munkafrekvencia megjelenítése ember által olvasható formátumban, a cpufreq kernelmodul szerint:

`cpufreq-info -f -m`

- Az aktuális CPU-munkafrekvencia megjelenítése ember által olvasható formátumban, a hardverből történő kiolvasással (csak a root számára elérhető):

`sudo cpufreq-info -w -m`
