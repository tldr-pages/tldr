# telnet

> Csatlakozás egy állomás megadott portjához a telnet protokoll segítségével. További információ: <https://manned.org/telnet>.

- Telnet egy állomás alapértelmezett portjára:

`telnet {{host}}`

- Telnet egy állomás meghatározott portjára:

`telnet {{ip_address}} {{port}}`

- Telnet-munkamenet kilépése:

`quit`

- A munkamenet befejezéséhez az alapértelmezett escape-karakterkombináció kiadása:

`Ctrl + ]`

- Telnet indítása "x" mint munkamenet befejező karakterrel:

`telnet -e {{x}} {{ip_address}} {{port}}`

- Telnet a Star Wars animációhoz:

`telnet {{towel.blinkenlights.nl}}`
