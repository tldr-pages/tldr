# ip stats

> Gestisce e mostra le statistiche dell'interfaccia.
> Maggiori informazioni: <https://manned.org/ip-stats>.

- Mostra tutte le statistiche dell'interfaccia su tutti i dispositivi di rete:

`ip {{[st|stats]}}`

- Mostra le statistiche per un'interfaccia di rete specifica:

`ip {{[st|stats]}} show dev {{network_interface}}`

- Mostra le statistiche del livello di collegamento (come `ip -statistics link show`):

`ip {{[st|stats]}} show group link`

- Mostra le statistiche di offload hardware per tutti i dispositivi:

`ip {{[st|stats]}} show group offload`

- Mostra le statistiche di offload per un'interfaccia specifica:

`ip {{[st|stats]}} show dev {{network_interface}} group offload`

- Mostra un sottogruppo di offload specifico:

`ip {{[st|stats]}} show dev {{network_interface}} group offload subgroup {{l3_stats|cpu_hit|hw_stats_info}}`

- Mostra statistiche specifiche per famiglia di indirizzi (es. MPLS):

`ip {{[st|stats]}} show group afstats subgroup {{mpls}}`

- Abilita la raccolta di statistiche hardware di Livello 3 su un dispositivo:

`ip {{[st|stats]}} set dev {{network_interface}} l3_stats on`
