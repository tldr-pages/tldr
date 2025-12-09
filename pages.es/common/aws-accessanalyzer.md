# aws accessanalyzer

> Analiza y revisa las políticas de recursos para identificar posibles riesgos de seguridad.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html>.

- Crea un nuevo Access Analyzer:

`aws accessanalyzer create-analyzer --analyzer-name {{nombre_analizador}} --type {{tipo}} --tags {{etiquetas}}`

- Elimina un analizador de acceso existente:

`aws accessanalyzer delete-analyzer --analyzer-arn {{analizador_arn}}`

- Obtiene detalles de un analizador de acceso específico:

`aws accessanalyzer get-analyzer --analyzer-arn {{analizador_arn}}`

- Lista todos los analizadores de acceso:

`aws accessanalyzer list-analyzers`

- Actualiza la configuración de un analizador de acceso:

`aws accessanalyzer update-analyzer --analyzer-arn {{analizador_arn}} --tags {{nuevas_etiquetas}}`

- Crea una nueva regla de archivo de Access Analyzer:

`aws accessanalyzer create-archive-rule --analyzer-arn {{analizador_arn}} --rule-name {{nombre_regla}} --filter {{filtro}}`

- Elimina una regla de archivo de Access Analyzer:

`aws accessanalyzer delete-archive-rule --analyzer-arn {{analizador_arn}} --rule-name {{nombre_regla}}`

- Lista todas las reglas de archivo de Access Analyzer:

`aws accessanalyzer list-archive-rules --analyzer-arn {{analizador_arn}}`
