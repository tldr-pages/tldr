# dockdiver

> Una herramienta para interactuar con registros Docker, incluyendo listar y volcar repositorios.
> Más información: <https://github.com/MachiavelliII/dockdiver>.

- Lista todos los repositorios en un registro Docker:

`dockdiver -url {{https://example.com}} -list`

- Vuelca un repositorio específico al directorio de salida por defecto (docker_dump):

`dockdiver -url {{https://example.com}} -dump {{nombre_repositorio}}`

- Vuelca todos los repositorios con autenticación básica:

`dockdiver -url {{http://example.com}} -dump-all -username {{nombre_usuario}} -password {{contraseña}}`

- Vuelca un repositorio con un puerto personalizado y un límite de velocidad:

`dockdiver -url http://example.com -dump {{nombre_repositorio}} -port {{puerto}} -rate {{solicitudes_por_segundo}} -dir {{ruta/a/directorio_salida}}`

- Vuelca todos los repositorios con token de portador para autorización:

`dockdiver -url {{http://example.com}} -dump-all -bearer {{bearer_token}}`

- Añade cabeceras personalizadas como JSON (por ejemplo, '{"X-Custom": "Value"}'):

`dockdiver -url {{http://example.com}} -list -headers {{'{"X-Custom": "Value"}'}}`
