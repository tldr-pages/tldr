# IPXNET

> Emuleer IPX-netwerken voor multiplayer-games (client-server-model).
> Meer informatie: <https://www.dosbox.com/wiki/Connectivity>.

- Start een IPX-server (standaard UDP-poort 213):

`IPXNET startserver`

- Start een server op een specifieke poort:

`IPXNET startserver {{19900}}`

- Maak verbinding als client met het IP-adres van een server:

`IPXNET connect {{192.168.2.100}}`

- Maak verbinding met een specifieke poort:

`IPXNET connect {{192.168.2.100}} {{19900}}`

- Controleer de netwerkstatus:

`IPXNET status`

- Ping om snelheid/clients te testen:

`IPXNET ping`

- Verbreek de verbinding van een client:

`IPXNET disconnect`

- Stop de server (nadat clients de verbinding hebben verbroken):

`IPXNET stopserver`
