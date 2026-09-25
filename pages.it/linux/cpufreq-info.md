# cpufreq-info

> Mostra le informazioni sulla frequenza della CPU.
> Maggiori informazioni: <https://manned.org/cpufreq-info>.

- Mostra le informazioni sulla frequenza della CPU per tutte le CPU:

`cpufreq-info`

- Mostra le informazioni sulla frequenza della CPU per la CPU specificata:

`cpufreq-info {{[-c|--cpu]}} {{cpu_number}}`

- Mostra la frequenza minima e massima consentita della CPU:

`cpufreq-info {{[-l|--hwlimits]}}`

- Mostra la frequenza minima e massima corrente della CPU e la politica in formato tabella:

`cpufreq-info {{[-o|--proc]}}`

- Mostra le politiche di frequenza della CPU disponibili:

`cpufreq-info {{[-g|--governors]}}`

- Mostra la frequenza di lavoro corrente della CPU in un formato leggibile, secondo il modulo kernel cpufreq:

`cpufreq-info {{[-f|--freq]}} {{[-m|--human]}}`

- Mostra la frequenza di lavoro corrente della CPU in un formato leggibile, leggendola dall'hardware (disponibile solo per root):

`sudo cpufreq-info {{[-w|--hwfreq]}} {{[-m|--human]}}`
