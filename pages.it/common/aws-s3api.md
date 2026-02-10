# aws s3api

> Crea ed elimina bucket Amazon S3 e modifica le proprietà del bucket.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/s3api/>.

- Crea un bucket in una regione specifica:

`aws s3api create-bucket --bucket {{nome_bucket}} --region {{regione}} --create-bucket-configuration LocationConstraint={{regione}}`

- Elimina un bucket:

`aws s3api delete-bucket --bucket {{nome_bucket}}`

- Elenca i bucket:

`aws s3api list-buckets`

- Elenca gli oggetti all'interno di un bucket e mostra solo la chiave e la dimensione di ciascun oggetto:

`aws s3api list-objects --bucket {{nome_bucket}} --query '{{Contents[].{Key: Key, Size: Size}}}'`

- Aggiunge un oggetto a un bucket:

`aws s3api put-object --bucket {{nome_bucket}} --key {{object_key}} --body {{percorso/del/file}}`

- Scarica un oggetto da un bucket (Il file di output è sempre l'ultimo argomento):

`aws s3api get-object --bucket {{nome_bucket}} --key {{object_key}} {{percorso/del/file_output}}`

- Applica una policy di bucket Amazon S3 a un bucket specificato:

`aws s3api put-bucket-policy --bucket {{nome_bucket}} --policy file://{{percorso/del/bucket_policy.json}}`

- Scarica la policy di bucket Amazon S3 da un bucket specificato:

`aws s3api get-bucket-policy --bucket {{nome_bucket}} --query Policy --output {{json|table|text|yaml|yaml-stream}} > {{percorso/del/bucket_policy}}`
