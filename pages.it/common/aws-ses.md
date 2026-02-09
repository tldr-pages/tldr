# aws ses

> CLI per AWS Simple Email Service.
> Servizio email cloud in ingresso e in uscita ad alta scala.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/ses/>.

- Crea un nuovo set di regole di ricezione:

`aws ses create-receipt-rule-set --rule-set-name {{nome_set_regole}} --generate-cli-skeleton`

- Descrivi il set di regole di ricezione attivo:

`aws ses describe-active-receipt-rule-set --generate-cli-skeleton`

- Descrivi una regola di ricezione specifica:

`aws ses describe-receipt-rule --rule-set-name {{nome_set_regole}} --rule-name {{nome_regola}} --generate-cli-skeleton`

- Elenca tutti i set di regole di ricezione:

`aws ses list-receipt-rule-sets --starting-token {{token_string}} --max-items {{integer}} --generate-cli-skeleton`

- Elimina un set di regole di ricezione specifico (il set di regole attualmente attivo non può essere eliminato):

`aws ses delete-receipt-rule-set --rule-set-name {{nome_set_regole}} --generate-cli-skeleton`

- Elimina una regola di ricezione specifica:

`aws ses delete-receipt-rule --rule-set-name {{nome_set_regole}} --rule-name {{nome_regola}} --generate-cli-skeleton`

- Invia un'email:

`aws ses send-email --from {{from_address}} --destination "ToAddresses={{addresses}}" --message "Subject={Data={{subject_text}},Charset=utf8},Body={Text={Data={{body_text}},Charset=utf8},Html={Data={{message_body_containing_html}},Charset=utf8}}"`

- Visualizza l'aiuto per un sottocomando SES specifico:

`aws ses {{subcommand}} help`
