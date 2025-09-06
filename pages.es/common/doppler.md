# doppler

> Gestiona variables de entorno a través de diferentes entornos usando Doppler.
> Algunos subcomandos como `run` y `secrets` tienen su propia documentación de uso.
> Más información: <https://docs.doppler.com/docs/cli>.

- Configura Doppler CLI en el directorio actual:

`doppler setup`

- Configura el proyecto Doppler y la configuración en el directorio actual:

`doppler setup`

- Ejecuta un comando con secretos inyectados en el entorno:

`doppler run --command {{comando}}`

- Visualiza la lista de proyectos:

`doppler projects`

- Visualiza los secretos del proyecto actual:

`doppler secrets`

- Abre el panel de control de doppler en el navegador:

`doppler open`
