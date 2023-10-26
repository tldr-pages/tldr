# nginx

> Servidor web Nginx.
> Mas información: <https://nginx.org/en/>.

- Iniciar el servidor con el archivo de configuración por defecto:

`nginx`

- Iniciar el servidor con un archivo de configuración personalizado:

`nginx -c {{archivo_de_configuración}}`

- Iniciar el servidor con un prefijo para todas las rutas relativas en el archivo de configuración:

`nginx -c {{archivo_de_configuración}} -p {{prefijo/para/rutas/relativas}}`

- Probar la configuración sin afectar al servidor en ejecución:

`nginx -t`

- Recarga la configuración enviando una señal sin tiempo de inactividad:

`nginx -s reload`
