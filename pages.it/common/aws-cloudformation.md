# aws cloudformation

> Modella, provisiona e gestisce risorse AWS e di terze parti trattando l'infrastruttura come codice.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/cloudformation/>.

- Crea uno stack da un file template:

`aws cloudformation create-stack --stack-name {{nome-stack}} --region {{regione}} --template-body {{file://percorso/del/file.yml}} --profile {{profilo}}`

- Elimina uno stack:

`aws cloudformation delete-stack --stack-name {{nome-stack}} --profile {{profilo}}`

- Elenca tutti gli stack:

`aws cloudformation list-stacks --profile {{profilo}}`

- Elenca tutti gli stack in esecuzione:

`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --profile {{profilo}}`

- Controlla lo stato di uno stack:

`aws cloudformation describe-stacks --stack-name {{id_stack}} --profile {{profilo}}`

- Avvia il rilevamento deriva per uno stack:

`aws cloudformation detect-stack-drift --stack-name {{id_stack}} --profile {{profilo}}`

- Controlla l'output dello stato deriva di uno stack usando `StackDriftDetectionId` dall'output del comando precedente:

`aws cloudformation describe-stack-resource-drifts --stack-name {{stack-drift-detection-id}} --profile {{profilo}}`
