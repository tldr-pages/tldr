# cpufreq-aperf

> Calcola la frequenza media della CPU in un periodo di tempo.
> Maggiori informazioni: <https://manned.org/cpufreq-aperf>.

- Avvia il calcolo, impostando come predefinito tutti i core della CPU e un intervallo di aggiornamento di 1 secondo:

`sudo cpufreq-aperf`

- Avvia il calcolo solo per la CPU 1:

`sudo cpufreq-aperf {{[-c|--cpu]}} {{1}}`

- Avvia il calcolo con un intervallo di aggiornamento di 3 secondi per tutti i core della CPU:

`sudo cpufreq-aperf {{[-i|--interval]}} {{3}}`

- Calcola solo una volta:

`sudo cpufreq-aperf {{[-o|--once]}}`
