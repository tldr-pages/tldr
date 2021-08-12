# pihole

> Interfață terminal pentru serverul DNS de blocare a anunțurilor PI-hole.
> Mai multe informaţii: <https://pi-hole.net>

- Verifică starea demonului găurii de Pi:

`pihole status`

- Actualizare PI-hole:

`pihole updatePihole`

- Monitorizarea stării detaliate a sistemului:

`pihole chronometer`

- Porniţi sau opriţi daemonul:

`pihole {{enable|disable}}`

- Reporniți daemonul (nu serverul în sine):

`pihole restartdns`

- Lista albă sau lista neagră a unui domeniu:

`pihole {{whitelist|blacklist}} {{example.com}}`

- Caută în liste pentru un domeniu:

`pihole query {{example.com}}`

- Deschide un jurnal de conexiuni în timp real:

`pihole tail`
