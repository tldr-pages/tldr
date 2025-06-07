# netsh interface portproxy

> Configurar y mostrar el estado de varios componentes de red.
> Más información: <https://learn.microsoft.com/windows-server/networking/technologies/netsh/netsh-interface-portproxy>.

- Mostrar la configuración actual de reenvío de puertos:

`netsh interface portproxy show all`

- Configurar el reenvío de puertos IPv4 (ejecutar en consola elevada):

`netsh interface portproxy add v4tov4 listenaddress={{192.168.0.1}} listenport={{8080}} connectaddress={{10.0.0.1}} connectport={{80}}`

- Eliminar el reenvío de puertos IPv4 (ejecutar en consola elevada):

`netsh interface portproxy delete v4tov4 listenaddress={{192.168.0.1}} listenport={{8080}}`

- Mostrar ayuda:

`netsh interface portproxy`
