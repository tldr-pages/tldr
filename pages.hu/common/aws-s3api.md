# aws s3api

> Amazon S3 vödrök létrehozása és törlése, valamint a vödrök tulajdonságainak szerkesztése. További információk: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html>.

- Vödör létrehozása egy adott régióban:

`aws s3api create-bucket --bucket {{bucket_name}} --region {{region}} --create-bucket-configuration LocationConstraint={{region}}`

- Vödör törlése:

`aws s3api delete-bucket --bucket {{bucket_name}}`

- Vödrök listázása:

`aws s3api list-buckets`

- A vödörben lévő objektumok listázása, és csak az egyes objektumok kulcsának és méretének megjelenítése:

`aws s3api list-objects --bucket {{bucket_name}} --query '{{Contents[].{Key: Key, Size: Size}}}'`

- Objektum hozzáadása egy vödörhöz:

`aws s3api put-object --bucket {{bucket_name}} --key {{object_key}} --body {{path/to/file}}`

- Objektum letöltése egy vödörből (A kimeneti fájl mindig az utolsó argumentum):

`aws s3api get-object --bucket {{bucket_name}} --key {{object_key}} {{path/to/output_file}}`

- Amazon S3 vödör házirend alkalmazása egy megadott vödörre:

`aws s3api put-bucket-policy --bucket {{bucket_name}} --policy file://{{path/to/bucket_policy.json}}`

- Az Amazon S3 vödör házirend letöltése egy megadott vödörből:

`aws s3api get-bucket-policy --bucket {{bucket_name}} --query Policy --output {{json|table|text|yaml|yaml-stream}} > {{path/to/bucket_policy}}`
