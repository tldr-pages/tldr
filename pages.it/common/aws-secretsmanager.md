# aws secretsmanager

> Memorizza, gestisce e recupera segreti.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>.

- Mostra i segreti memorizzati dal secrets manager nell'account corrente:

`aws secretsmanager list-secrets`

- Elenca tutti i segreti ma mostra solo i nomi dei segreti e gli ARN (facile da visualizzare):

`aws secretsmanager list-secrets --query 'SecretList[*].{Name: Name, ARN: ARN}'`

- Crea un segreto:

`aws secretsmanager create-secret --name {{name}} --description "{{secret_description}}" --secret-string '{{segreto}}'`

- Elimina un segreto (aggiungi `--force-delete-without-recovery` per eliminare immediatamente senza periodo di recupero):

`aws secretsmanager delete-secret --secret-id {{nome|arn}}`

- Visualizza i dettagli di un segreto escluso il testo del segreto:

`aws secretsmanager describe-secret --secret-id {{nome|arn}}`

- Recupera il valore di un segreto (per ottenere l'ultima versione del segreto ometti `--version-stage`):

`aws secretsmanager get-secret-value --secret-id {{nome|arn}} --version-stage {{versione_del_segreto}}`

- Ruota il segreto immediatamente utilizzando una funzione Lambda:

`aws secretsmanager rotate-secret --secret-id {{nome|arn}} --rotation-lambda-arn {{arn_della_funzione_lambda}}`

- Ruota il segreto automaticamente ogni 30 giorni utilizzando una funzione Lambda:

`aws secretsmanager rotate-secret --secret-id {{nome|arn}} --rotation-lambda-arn {{arn_della_funzione_lambda}} --rotation-rules AutomaticallyAfterDays={{30}}`
