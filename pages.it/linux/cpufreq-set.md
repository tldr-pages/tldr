# cpufreq-set

> Uno strumento per modificare le impostazioni della frequenza della CPU.
> Il valore della frequenza deve essere compreso tra l'output del comando `cpufreq-info -l`.
> Maggiori informazioni: <https://manned.org/cpufreq-set>.

- Imposta la politica di frequenza della CPU del core 1 su "userspace":

`sudo cpufreq-set {{[-c|--cpu]}} {{1}} {{[-g|--governor]}} {{userspace}}`

- Imposta la frequenza minima corrente della CPU del core 1:

`sudo cpufreq-set {{[-c|--cpu]}} {{1}} {{[-d|--min]}} {{min_frequency}}`

- Imposta la frequenza massima corrente della CPU del core 1:

`sudo cpufreq-set {{[-c|--cpu]}} {{1}} {{[-u|--max]}} {{max_frequency}}`

- Imposta la frequenza di lavoro corrente della CPU del core 1:

`sudo cpufreq-set {{[-c|--cpu]}} {{1}} {{[-f|--freq]}} {{work_frequency}}`
