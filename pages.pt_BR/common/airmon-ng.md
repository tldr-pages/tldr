# airmon-ng

> Ativa modo de monitoramento em dispositivos de rede sem-fio.
> Mais informações: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Lista os dispositivos sem-fio e seus respectivos estados:

`sudo airmon-ng`

- Liga o modo de monitoramento para um dispositivo específico:

`sudo airmon-ng start {{wlan0}}`

- Encerra processos problemáticos que usam dispositivos sem-fio:

`sudo airmon-ng check kill`

- Desativa o modo de monitoramento para um dispositivo específico:

`sudo airmon-ng stop {{wlan0mon}}`
