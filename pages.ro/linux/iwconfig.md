# iwconfig

> Configurați și afișați parametrii unei interfețe de rețea fără fir.
> Mai multe informaţii: <https://manned.org/iwconfig>

- Afișați parametrii și statisticile tuturor interfețelor:

`iwconfig`

- Afișați parametrii și statisticile interfeței specificate:

`iwconfig {{interface}}`

- Setați ESSID (numele rețelei) interfeței specificate (de exemplu, eth0 sau wlp2s0):

`iwconfig {{interface}} {{new_network_name}}`

- Setați modul de funcționare al interfeței specificate:

`iwconfig {{interface}} mode {{ad hoc|Managed|Master|Repeater|Secondary|Monitor|Auto}}`
