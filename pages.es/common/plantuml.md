# plantuml

> Crea diagramas UML a partir de un lenguaje de texto plano y los renderiza en diferentes formatos.
> Más información: <https://plantuml.com/en/command-line>.

- Renderiza los diagramas al formato por defecto (PNG):

`plantuml {{diagrama1.puml}} {{diagrama2.puml}}`

- Renderiza un diagrama en un formato determinado (p.ej. `png`, `pdf`, `svg`, `txt`):

`plantuml -t {{formato}} {{diagrama.puml}}`

- Renderiza todos los diagramas de un directorio:

`plantuml {{ruta/a/diagramas}}`

- Renderiza un diagrama al directorio de salida:

`plantuml -o {{ruta/a/salida}} {{diagrama.puml}}`

- Renderiza un diagrama sin almacenar el código fuente del diagrama (Nota: Se almacena por defecto cuando no se especifica la opción `-nometadata`):

`plantuml -nometadata {{diagrama.png}} > {{diagrama.puml}}`

- Recupera la fuente de los metadatos de un diagrama `plantuml`:

`plantuml -metadata {{diagrama.png}} > {{diagrama.puml}}`

- Renderiza un diagrama con el archivo de configuración:

`plantuml -config {{config.cfg}} {{diagrama.puml}}`

- Muestra la ayuda:

`plantuml -help`
