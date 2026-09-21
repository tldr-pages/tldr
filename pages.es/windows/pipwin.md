# pipwin

> Una herramienta para instalar binarios de paquetes de Python no oficiales en Windows.
> Más información: <https://github.com/lepisma/pipwin>.

- Lista todos los paquetes disponibles para descargar:

`pipwin list`

- Busca paquetes:

`pipwin search {{nombre_parcial|nombre}}`

- Instalar un paquete:

`pipwin install {{paquete}}`

- Desinstalar un paquete:

`pipwin uninstall {{paquete}}`

- Descargar un paquete a un directorio específico:

`pipwin download --dest {{ruta\al\directorio}} {{paquete}}`

- Instala paquetes de acuerdo a `requirements.txt`:

`pipwin install --file {{ruta\al\requirements.txt}}`
