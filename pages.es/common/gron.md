# gron

> Transforma `JSON` en asignaciones individuales para una gestión más sencilla.
> Más información: <https://manned.org/gron>.

- Transforma el archivo `JSON` en asignaciones individuales:

`gron {{ruta/al/archivo|url}}`

- No ordena los datos de salida:

`gron --no-sort {{ruta/al/archivo|url}}`

- Desactiva la validación de certificados:

`gron {{[-k|--insecure]}} {{url}}`

- Muestra los valores de las asignaciones de `gron`:

`gron {{[-v|--values]}} {{ruta/al/archivo|url}}`

- Convierte las asignaciones convertidas con `gron` en `JSON`:

`gron {{[-u|--ungron]}} {{ruta/al/archivo|url}}`

- Procesa líneas individuales de entrada como objetos `JSON` separados:

`gron {{[-s|--stream]}} {{ruta/al/archivo|url}}`

- Representa los datos procesados como un flujo `JSON`:

`gron {{[-j|--json]}} {{ruta/al/archivo|url}}`
