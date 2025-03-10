# tcpreplay

> Reproduce el tráfico de red almacenado en un archivo `pcap`.
> Más información: <https://tcpreplay.appneta.com/>.

- Lista las interfaces de red disponibles:

`tcpreplay --listnics`

- Reproduce el tráfico de la interface:

`tcpreplay -i {{eth0}} {{tráfico.pcap}}`

- Reproduce tráfico en la interface y en `stdout`:

`tcpreplay -i {{eth0}} --verbose {{tráfico.pcap}}`

- Reproduce el tráfico en la interface lo más rápido posible:

`tcpreplay -i {{eth0}} --topspeed {{tráfico.pcap}}`

- Reproduce el tráfico en la interface a los Mbps indicados:

`tcpreplay -i {{eth0}} -M {{10}} {{tráfico.pcap}}`

- Reproduce el tráfico en la interface varias veces:

`tcpreplay -i {{eth0}} --loop={{número_veces}} {{tráfico.pcap}}`
