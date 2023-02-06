# ansiweather

> Egy shell script az aktuális időjárási viszonyok megjelenítésére a terminálon. További információ: <https://github.com/fcambus/ansiweather>.

- A következő öt napra vonatkozó előrejelzés megjelenítése metrikus mértékegységekben a lengyelországi Rzeszow számára:

`ansiweather -u {{metric}} -f {{5}} -l {{Rzeszow,PL}}`

- Egy szimbólumokat és napfényadatokat mutató előrejelzés megjelenítése az Ön aktuális tartózkodási helyére:

`ansiweather -s {{true}} -d {{true}}`

- Szél- és páratartalom-adatokat mutató előrejelzés megjelenítése az Ön aktuális tartózkodási helyére:

`ansiweather -w {{true}} -h {{true}}`
