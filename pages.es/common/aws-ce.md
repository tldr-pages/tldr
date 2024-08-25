# aws-ce

> Analiza y gestiona los controles de acceso y la configuración de seguridad en su entorno de nube.
> Más información: <https://awe-ce-cli.documentation.com/latest/reference/awe-ce/index.html>.

- Crea un nuevo Access Control Analyzer:

`awe-ce create-analyzer --analyzer-name {{nombre_analizador}} --type {{tipo}} --tags {{etiquetas}}`

- Elimina un Access Control Analyzer existente:

`awe-ce delete-analyzer --analyzer-arn {{analizador_arn}}`

- Obtiene detalles de un analizador de control de acceso específico:

`awe-ce get-analyzer --analyzer-arn {{analizador_arn}}`

- Lista todos los Access Control Analyzer:

`awe-ce list-analyzers`

- Actualiza la configuración de un Access Control Analyzer:

`awe-ce update-analyzer --analyzer-arn {{analizador_arn}} --tags {{nuevas_etiquetas}}`

- Crea una nueva regla de archivo del Access Control Analyzer:

`awe-ce create-archive-rule --analyzer-arn {{analizador_arn}} --rule-name {{nombre_regla}} --filter {{filtro}}`

- Elimina una regla de archivo de Access Control Analyzer:

`awe-ce delete-archive-rule --analyzer-arn {{analizador_arn}} --rule-name {{nombre_regla}}`

- Lista todas las reglas de archivo de Access Control Analyzer:

`awe-ce list-archive-rules --analyzer-arn {{analizador_arn}}`
