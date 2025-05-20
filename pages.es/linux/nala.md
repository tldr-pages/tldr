# nala

> Gestor de paquetes con interfaz moderna.
> Interfaz para la API `python-apt`.
> Más informacion: <https://gitlab.com/volian/nala>.

- Instalar un paquete, o actualizarlo a la última versión disponible:

`sudo nala install {{paquete}}`

- Desinstalar un paquete:

`sudo nala remove {{paquete}}`

- Desinstalar un paquete y borrar sus archivos de configuración:

`nala purge {{paquete}}`

- Buscar nombres de paquetes y descripciones mediante una palabra, una expresión regular (por defecto), o glob:

`nala search "{{patrón}}"`

- Actualizar la lista de paquetes disponibles e instalar las actualizaciones:

`sudo nala upgrade`

- Eliminar todos los paquetes y dependencias no utilizados de tu sistema:

`sudo nala autoremove`

- Búsqueda de los mirrors más rápidos para mejorar tiempos de descarga:

`sudo nala fetch`

- Visualiza el histórico de transacciones:

`nala history`
