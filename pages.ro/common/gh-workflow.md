# gh workflow

> Listați, vizualizați și executați fluxurile de lucru Acțiuni GitHub.
> Mai multe informaţii: <https://cli.github.com/manual/gh_workflow>

- Selectați interactiv un flux de lucru pentru a vizualiza cele mai recente lucrări pentru:

`gh workflow view`

- Vizualizați un anumit flux de lucru în browserul implicit:

`gh workflow view {{id|workflow_name|filename.yml}} --web`

- Afișează definiția YAML a unui anumit flux de lucru:

`gh workflow view {{id|workflow_name|filename.yml}} --yaml`

- Afișează definiția YAML pentru o anumită ramură Git sau etichetă:

`gh workflow view {{id|workflow_name|filename.yml}} --ref {{branch_or_tag_name}} --yaml`

- Listă fișiere de flux de lucru (utilizați `—all` pentru a include fluxuri de lucru dezactivate):

`gh workflow list`

- Rulați un flux de lucru manual cu parametri:

`gh workflow run {{id|workflow_name|filename.yml}} --raw-field {{param1}}={{value1}} --raw-field {{param2}}={{value2}}`

- Rulați un flux de lucru manual utilizând o ramură sau o etichetă specifică cu parametrii JSON de la stdin:

`echo '{{{"param1":"value1", "param2":"value2"}}}' | gh workflow run {{id|workflow_name|filename.yml}} --ref {{branch_or_tag_name}}`

- Activați sau dezactivați un anumit flux de lucru:

`gh workflow {{enable|disable}} {{id|workflow_name|filename.yml}}`
