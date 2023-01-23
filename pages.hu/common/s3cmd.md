# s3cmd

> Parancssori eszköz és kliens az S3 kompatibilis objektumtárolóba történő adatfeltöltéshez, -lehíváshoz és -kezeléshez. További információ: <https://s3tools.org/s3cmd>.

- Konfigurációs/rekonfigurációs eszköz meghívása:

`s3cmd --configure`

- List Buckets/Folders/Objects:

`s3cmd ls s3://{{bucket|path/to/file}}`

- Bucket/Mappa létrehozása:

`s3cmd mb s3://{{bucket}}`

- Egy adott fájl letöltése egy vödörből:

`s3cmd get s3://{{bucket_name}}/{{path/to/file}} {{path/to/local_file}}`

- Fájl feltöltése egy vödörbe:

`s3cmd put {{local_file}} s3://{{bucket}}/{{file}}`

- Objektum áthelyezése egy adott vödörbe:

`s3cmd mv s3://{{src_bucket}}/{{src_object}} s3://{{dst_bucket}}/{{dst_object}}`

- Egy adott objektum törlése:

`s3cmd rm s3://{{bucket}}/{{object}}`
