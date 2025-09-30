# http

> HTTPie: un cliente HTTP diseñado para probar, depurar e interactuar generalmente con APIs y servidores HTTP.
> Más información: <https://httpie.io/docs/cli/usage>.

- Hace una solicitud simple GET (muestra encabezados de respuesta y contenido):

`http {{https://example.com}}`

- Imprime partes específicas del contenido (`H`: encabezados de la solicitud, `B`: cuerpo de la solicitud, `h`: encabezados de la respuesta, `b`: cuerpo de la respuesta, `m`: metadatos de respuesta):

`http {{[-p|--print]}} {{H|B|h|b|m|Hh|Hhb|...}} {{https://example.com}}`

- Especifica el método HTTP al enviar una solicitud y utiliza un proxy para interceptar la solicitud:

`http {{GET|POST|HEAD|PUT|PATCH|DELETE|...}} --proxy {{http|https}}:{{http://localhost:8080|socks5://localhost:9050|...}} {{https://example.com}}`

- Sigue cualquier redirección `3xx` y especifica encabezados adicionales en una solicitud:

`http {{[-F|--follow]}} {{https://example.com}} {{'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'}}`

- Autentica ante un servidor utilizando diferentes métodos de autenticación:

`http {{[-a|--auth]}} {{username:password|token}} {{[-A|--auth-type]}} {{basic|digest|bearer}} {{GET|POST|...}} {{https://example.com/auth}}`

- Construye una solicitud pero no la envía (similar a un simulacro (dry-run)):

`http --offline {{GET|DELETE|...}} {{https://example.com}}`

- Utiliza sesiones nombradas para encabezados personalizados persistentes, credenciales de autenticación y cookies:

`http --session {{nombre_de_sesión|ruta/a/sesión.json}} {{[-a|--auth]}} {{usuario}}:{{clave}} {{https://example.com/auth}} {{API-KEY:xxx}}`

- Sube un archivo a un formulario (el ejemplo a continuación supone que el campo del formulario es `<input type="file" name="cv" />`):

`http {{[-f|--form]}} {{POST}} {{https://example.com/upload}} {{cv@ruta/al/archivo}}`
