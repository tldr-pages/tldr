# apachectl

> Controla un servidor HTTP Apache.
> Más información: <https://manned.org/apachectl>.

- Inicia el servidor:

`sudo apachectl start`

- Reinicia el servidor:

`sudo apachectl restart`

- Detiene el servidor:

`sudo apachectl stop`

- Comprueba la validez del archivo de configuración:

`apachectl configtest`

- Comprueba el estado del servidor (requiere el navegador lynx):

`apachectl status`

- Recarga la configuración sin perder conexiones:

`sudo apachectl graceful`

- Imprime la configuración completa de Apache:

`apachectl -S`

- Muestra la ayuda:

`apachectl -h`
