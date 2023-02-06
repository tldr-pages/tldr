# aws s3 ls

> Az AWS S3 vödrök, mappák (előtagok) és fájlok (objektumok) listázása. További információk: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/ls.html>.

- Az összes vödör listázása:

`aws s3 ls`

- Fájlok és mappák listázása egy vödör gyökerében (`s3://` opcionális):

`aws s3 ls s3://{{bucket_name}}`

- Fájlok és mappák listázása közvetlenül egy könyvtáron belül:

`aws s3 ls {{bucket_name}}/{{path/to/directory}}/`

- Egy vödörben lévő összes fájl listázása:

`aws s3 ls --recursive {{bucket_name}}`

- Egy adott előtaggal rendelkező útvonal összes fájljának listázása:

`aws s3 ls --recursive {{bucket_name}}/{{path/to/directory/}}{{prefix}}`

- Súgó megjelenítése:

`aws s3 ls help`
