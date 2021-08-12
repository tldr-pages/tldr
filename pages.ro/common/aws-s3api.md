# aws s3api

> Creați și ștergeți găleți Amazon S3 și editați proprietățile găleții.
> Mai multe informaţii: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html>

- Creează o găleată:

`aws s3api create-bucket --bucket {{bucket_name}}`

- Şterge o găleată:

`aws s3api delete-bucket --bucket {{bucket_name}}`

- Lista găleților:

`aws s3api list-buckets`

- Listați obiectele din interiorul unei găleți și afișați doar cheia și dimensiunea fiecărui obiect:

`aws s3api list-objects --bucket {{bucket_name}} --query '{{Contents[].{Key: Key, Size: Size}}}'`

- Adaugă un obiect într-o găleată:

`aws s3api put-object --bucket {{bucket_name}} --key {{object_key}} --body {{path/to/file}}`

- Descărcați obiectul dintr-o găleată (Fișierul de ieșire este întotdeauna ultimul argument):

`aws s3api get-object --bucket {{bucket_name}} --key {{object_key}} {{path/to/output_file}}`

- Aplicați o politică a cupei Amazon S3 la o găleată specificată:

`aws s3api put-bucket-policy --bucket {{bucket_name}} --policy file://{{path/to/bucket_policy.json}}`

- Descărcați politica de cupă Amazon S3 dintr-o găleată specificată:

`aws s3api get-bucket-policy --bucket {{bucket_name}} --query Policy --output {{json|table|text|yaml|yaml-stream}} > {{path/to/bucket_policy}}`
