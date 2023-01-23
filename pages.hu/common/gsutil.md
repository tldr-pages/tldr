# gsutil

> A gsutil CLI segítségével parancssorból érheti el a Google Cloud Storage-t. A gsutil segítségével a vödrök és objektumok kezelésével kapcsolatos feladatok széles körét végezheti el. További információk: <https://cloud.google.com/storage/docs/gsutil>.

- A projektben lévő összes bucket listázása, amelybe bejelentkezett:

`gsutil ls`

- Egy vödörben lévő objektumok listázása:

`gsutil ls -r 'gs://{{bucket_name}}/{{prefix}}**'`

- Objektum letöltése egy vödörből:

`gsutil cp gs://{{bucket_name}}/{{object_name}} {{path/to/save_location}}`

- Objektum feltöltése egy vödörbe:

`gsutil cp {{object_location}} gs://{{destination_bucket_name}}/`

- Objektumok átnevezése vagy áthelyezése egy vödörben:

`gsutil mv gs://{{bucket_name}}/{{old_object_name}} gs://{{bucket_name}}/{{new_object_name}}`

- Új vödör létrehozása a projektben, amelybe bejelentkezett:

`gsutil mb gs://{{bucket_name}}`

- Egy vödör törlése és a benne lévő összes objektum eltávolítása:

`gsutil rm -r gs://{{bucket_name}}`
