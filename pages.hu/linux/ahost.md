# ahost

> DNS kereső segédprogram a hostnévhez vagy IP-címhez kapcsolódó A vagy AAAA rekordok megjelenítéséhez. További információ: <https://manned.org/ahost>.

- Egy gazdanévhez vagy IP-címhez kapcsolódó `A` vagy `AAAA` rekord kinyomtatása:

`ahost {{example.com}}`

- Néhány extra hibakeresési kimenet megjelenítése:

`ahost -d {{example.com}}`

- A megadott típusú rekord megjelenítése:

`ahost -t {{a|aaaa|u}} {{example.com}}`
