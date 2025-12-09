# dumpsys

> Suministra información sobre los servicios del sistema Android.
> Este comando solo se puede usar a través de `adb shell`.
> Más información: <https://developer.android.com/tools/dumpsys>.

- Obtén los resultados de diagnóstico para todos los servicios del sistema:

`dumpsys`

- Obtén los resultados de diagnóstico para un servicio de sistema específico:

`dumpsys {{service}}`

- Enumera todos los servicios que `dumpsys` sobre los que puede proporcionar información:

`dumpsys -l`

- Enumera los argumentos específicos del servicio para un servicio determinado:

`dumpsys {{service}} -h`

- Excluye un servicio específico de la salida de diagnóstico:

`dumpsys --skip {{service}}`

- Especifica un período de tiempo de espera en segundos (predeterminado en 10 segundos):

`dumpsys -t {{seconds}}`
