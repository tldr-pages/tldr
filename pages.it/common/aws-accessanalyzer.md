# aws accessanalyzer

> Analizza e rivedi le policy delle risorse per identificare potenziali rischi per la sicurezza.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/>.

- Crea un nuovo Access Analyzer:

`aws accessanalyzer create-analyzer --analyzer-name {{nome_analizzatore}} --type {{tipo}} --tags {{tag}}`

- Elimina un Access Analyzer esistente:

`aws accessanalyzer delete-analyzer --analyzer-arn {{arn_analizzatore}}`

- Ottiene i dettagli di un Access Analyzer specifico:

`aws accessanalyzer get-analyzer --analyzer-arn {{arn_analizzatore}}`

- Elenca tutti gli Access Analyzer:

`aws accessanalyzer list-analyzers`

- Aggiorna le impostazioni di un Access Analyzer:

`aws accessanalyzer update-analyzer --analyzer-arn {{arn_analizzatore}} --tags {{nuovi_tag}}`

- Crea una nuova regola di archiviazione per un Access Analyzer:

`aws accessanalyzer create-archive-rule --analyzer-arn {{arn_analizzatore}} --rule-name {{nome_regola}} --filter {{filtro}}`

- Elimina una regola di archiviazione di un Access Analyzer:

`aws accessanalyzer delete-archive-rule --analyzer-arn {{arn_analizzatore}} --rule-name {{nome_regola}}`

- Elenca tutte le regole di archiviazione di un Access Analyzer:

`aws accessanalyzer list-archive-rules --analyzer-arn {{arn_analizzatore}}`
