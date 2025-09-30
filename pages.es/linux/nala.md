# nala

> Gestor de paquetes con interfaz moderna.
> Interfaz para la API `python-apt`.
> Más información: <https://gitlab.com/volian/nala>.

- Instala un paquete o lo actualiza a la última versión disponible:

`sudo nala install {{paquete}}`

- Desinstala un paquete:

`sudo nala remove {{paquete}}`

- Desinstala un paquete y borra sus archivos de configuración:

`nala purge {{paquete}}`

- Busca nombres de paquetes y sus descripciones mediante una palabra, una expresión regular (por defecto) o mediante glob:

`nala search "{{patrón}}"`

- Actualiza la lista de paquetes disponibles e instala las actualizaciones:

`sudo nala upgrade`

- Elimina todos los paquetes y dependencias no utilizados de tu sistema:

`sudo nala autoremove`

- Búsqueda de los espejos más rápidos para mejorar tiempos de descarga:

`sudo nala fetch`

- Visualiza el histórico de transacciones:

`nala history`
