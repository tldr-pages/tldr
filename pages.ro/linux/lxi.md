# lxi

> Control instrumente compatibile LXI, cum ar fi osciloscoapele.
> Mai multe informaţii: <https://github.com/lxi-tools/lxi-tools>

- Descoperiți dispozitivele LXI în rețelele disponibile:

`lxi discover`

- Capturați o captură de ecran, detectând automat un plugin:

`lxi screenshot --address {{ip_address}}`

- Capturați o captură de ecran utilizând un plugin specificat:

`lxi screenshot --address {{ip_address}} --plugin {{rigol-1000z}}`

- Trimiteți o comandă SCPI la un instrument:

`lxi scpi --address {{ip_address}} "{{*IDN?}}"`

- Rulați un criteriu de referință pentru performanța solicitărilor și răspunsului:

`lxi benchmark --address {{ip_address}}`
