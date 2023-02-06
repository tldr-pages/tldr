# adig

> A Domain Name System (DNS) szerverektől kapott információk nyomtatása. További információ: <https://manned.org/adig>.

- A (alapértelmezett) rekord megjelenítése a DNS-ből az állomásnév(ek)re vonatkozóan:

`adig {{example.com}}`

- Extra \[d\]ebugging kimenet megjelenítése:

`adig -d {{example.com}}`

- Csatlakozás egy adott DNS \[s\]erverhez:

`adig -s {{1.2.3.4}} {{example.com}}`

- Egy adott TCP-port használata a DNS-kiszolgálóhoz való csatlakozáshoz:

`adig -T {{port}} {{example.com}}`

- Egy adott UDP-port használata a DNS-kiszolgálóhoz való csatlakozáshoz:

`adig -U {{port}} {{example.com}}`
