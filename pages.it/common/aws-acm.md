# aws acm

> AWS Certificate Manager.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/acm/>.

- Importa un certificato:

`aws acm import-certificate --certificate-arn {{arn_certificato}} --certificate {{certificato}} --private-key {{chiave_privata}} --certificate-chain {{catena_certificati}}`

- Elenca i certificati:

`aws acm list-certificates`

- Descrive un certificato:

`aws acm describe-certificate --certificate-arn {{arn_certificato}}`

- Richiede un certificato:

`aws acm request-certificate --domain-name {{nome_dom}} --validation-method {{metodo_validazione}}`

- Elimina un certificato:

`aws acm delete-certificate --certificate-arn {{arn_certificato}}`

- Elenca le convalide dei certificati (usa `--certificate-statuses {{stato}}` con `list-certificates`):

`aws acm list-certificates --certificate-statuses {{stato}}`

- Ottiene i dettagli di un certificato:

`aws acm get-certificate --certificate-arn {{arn_certificato}}`

- Aggiorna le opzioni di un certificato:

`aws acm update-certificate-options --certificate-arn {{arn_certificato}} --options {{opzioni}}`
