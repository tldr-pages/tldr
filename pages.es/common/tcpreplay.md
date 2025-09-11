# tcpreplay

> Reproduce el tráfico de red almacenado en un archivo `pcap`.
> Más información: <https://tcpreplay.appneta.com/wiki/tcpreplay-man.html>.

- Lista las interfaces de red disponibles:

`tcpreplay --listnics`

- Reproduce el tráfico de la interface:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{tráfico.pcap}}`

- Reproduce tráfico en la interface y en `stdout`:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-v|--verbose]}} {{tráfico.pcap}}`

- Reproduce el tráfico en la interface lo más rápido posible:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-t|--topspeed]}} {{tráfico.pcap}}`

- Reproduce el tráfico en la interface a los Mbps indicados:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-M|--mbps]}} {{10}} {{tráfico.pcap}}`

- Reproduce el tráfico en la interface varias veces:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-l|--loop]}} {{número_veces}} {{tráfico.pcap}}`
