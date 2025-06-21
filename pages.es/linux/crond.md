# crond

> Programa residente para ejecutar comandos programados desde archivos crontab.
> Más información: <https://manned.org/crond>.

- Inicia el programa residente en segundo plano y comprueba los comandos programados:

`crond`

- Inicia el programa residente en primer plano y comprueba los comandos programados:

`crond -n`

- Envía la salida del trabajo desde el programa residente al registro del sistema:

`crond -s`

- Anula las limitaciones predeterminadas y acepta crontables personalizados:

`crond -p`

- Hereda la ruta del archivo crontab desde la configuración del entorno:

`crond -P`
