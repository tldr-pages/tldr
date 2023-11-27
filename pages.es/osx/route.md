# route

> Manipula manualmente las tablas de enrutamiento.
> Necesita ser root.
> Más información: <https://www.manpagez.com/man/8/route/>.

- Añade una ruta a un destino a través de una puerta de enlace:

`sudo route add "{{dirección_ip_destino}}" "{{dirección_puerta}}"`

- Añade una ruta a una subred /24 a través de una puerta de enlace:

`sudo route add "{{dirección_ip_subred}}/24" "{{dirección_puerta}}"`

- Ejecuta en modo de prueba (no hace nada, sólo imprime):

`sudo route -t add "{{dirección_ip_destino}}/24" "{{dirección_puerta}}"`

- Elimina todas las rutas:

`sudo route flush`

- Elimina una ruta específica:

`sudo route delete "{{dirección_ip_destino}}/24"`

- Busca y muestra la ruta de un destino (nombre de host o dirección IP):

`sudo route get "{{destino}}"`
