# lshw

> Muestra información detallada sobre la configuración del hardware como usuario root.
> Vea también: `inxi`, `hwinfo`, `dmidecode`.
> Más información: <https://ezix.org/project/wiki/HardwareLiSter>.

- Inicia la interfaz gráfica X11 (si está disponible):

`sudo lshw -X`

- Muestra todo el hardware en formato tabular:

`sudo lshw -short`

- Muestra varias clases de hardware (todos los discos y controladores de almacenamiento) en formato tabular:

`sudo lshw {{[-c|-class]}} disk {{[-c|-class]}} storage -short`

- Guarda todas las interfaces de red en un archivo HTML/XML/JSON:

`sudo lshw {{[-c|-class]}} network -{{html|xml|json}} > interfaces{{.html|.xml|.json}}`

- Muestra las interfaces de red sin revelar información confidencial (direcciones IP, números de serie, etc.):

`sudo lshw {{[-c|-class]}} network -sanitize`

- Muestra una clase concreta de hardware:

`sudo lshw {{[-c|-class]}} {{system|bridge|memory|processor|address|storage|disk|tape|bus|network|display|input|printer|multimedia|communication|power|volume|generic}}`
