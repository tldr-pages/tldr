# valkey-server

> Base de datos clave-valor en memoria.
> Más información: <https://valkey.io/topics/server/>.

- Iniciar el servidor Valkey usando el puerto predeterminado (6379) y escribir los registros en `stdout`:

`valkey-server`

- Iniciar el servidor Valkey usando el puerto predeterminado como proceso en segundo plano:

`valkey-server --daemonize yes`

- Iniciar el servidor Valkey usando un puerto específico como proceso en segundo plano:

`valkey-server --port {{puerto}} --daemonize yes`

- Iniciar el servidor Valkey con un archivo de configuración personalizado:

`valkey-server {{ruta/al/valkey.conf}}`

- Iniciar el servidor Valkey con registro detallado:

`valkey-server --loglevel {{warning|notice|verbose|debug}}`
