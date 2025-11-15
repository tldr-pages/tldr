# scriptlive

> Ejecuta un typescript creado por el comando `script` en tiempo real.
> Vea también: `script`.
> Más información: <https://manned.org/scriptlive>.

- Ejecuta un typescript en tiempo real:

`scriptlive {{ruta/al/archivo_de_tiempo}} {{ruta/a/typescript}}`

- Ejecuta un typescript al doble de la velocidad original:

`scriptlive {{ruta/al/archivo_de_timing}} {{ruta/a/typescript}} --divisor 2`

- Ejecuta un guión tipográfico creado con la opción `--log-in` de `script`:

`scriptlive --log-in {{ruta/al/archivo_de_registro}} {{ruta/a/typescript}}`

- Ejecuta un typescript esperando como máximo 2 segundos entre cada comando:

`scriptlive {{ruta/al/archivo_de_tiempo}} {{ruta/a/typescript}} --maxdelay 2`
