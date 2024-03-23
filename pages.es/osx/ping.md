# ping

> Envía paquetes ICMP ECHO_REQUEST a hosts de la red.
> Más información: <https://keith.github.io/xcode-man-pages/ping.8.html>.

- Ping al host especificado:

`ping "{{hostname}}"`

- Ping a un host un número determinado de veces:

`ping -c {{cuenta}} "{{host}}"`

- Ping al `host`, especificando el intervalo en `segundos` entre peticiones (por defecto es 1 segundo):

`ping -i {{segundos}} "{{host}}"`

- Ping a `host` sin intentar buscar nombres simbólicos para las direcciones:

`ping -n "{{host}}"`

- Ping al `host` y hace sonar la campana cuando se recibe un paquete (si tu terminal lo soporta):

`ping -a "{{host}}"`

- Ping al `host` y muestra la hora en la que se ha recibido un paquete (esta opción es un añadido de Apple):

`ping --apple-time "{{host}}"`
