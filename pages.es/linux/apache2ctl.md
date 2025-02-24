# apache2ctl

> Administra el servidor web Apache HTTP.
> Este comando viene con los sistemas operativos basados en Debian; para los basados en RHEL, consulte `httpd`.
> Más información: <https://manned.org/apache2ctl.8>.

- Inicia el programa residente (daemon) de Apache. Muestra un mensaje si ya está en ejecución:

`sudo apache2ctl start`

- Detiene el programa residente (daemon) de Apache:

`sudo apache2ctl stop`

- Reinicia el programa residente (daemon) de Apache:

`sudo apache2ctl restart`

- Prueba la sintaxis del archivo de configuración:

`sudo apache2ctl -t`

- Lista los módulos cargados:

`sudo apache2ctl -M`
