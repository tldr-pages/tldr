#կոպիա

> Արագ, անվտանգ բաց կոդով պահուստավորման գործիք:.
> Աջակցում է կոդավորումը, սեղմումը, կրկնօրինակումը և աճող նկարները:.
> Լրացուցիչ տեղեկություններ. <https://kopia.io/docs/reference/command-line/>:.

- Ստեղծեք պահեստ տեղական ֆայլային համակարգում.:

`kopia repository create filesystem --path {{path/to/local_repository}}`

- Ստեղծեք պահեստ Amazon S3-ում.:

`kopia repository create s3 --bucket {{bucket_name}} --access-key {{AWS_access_key_id}} --secret-access-key {{AWS_secret_access_key}}`

- Միացեք պահեստին.:

`kopia repository connect {{repository_type}} --path {{path/to/repository}}`

- Ստեղծեք գրացուցակի պատկեր.:

`kopia snapshot create {{path/to/directory}}`

- Ցուցակ պատկերներ.:

`kopia snapshot list`

- Վերականգնել լուսանկարը որոշակի գրացուցակում.:

`kopia snapshot restore {{snapshot_id}} {{path/to/target_directory}}`

- Ստեղծեք նոր քաղաքականություն.:

`kopia policy set --global --keep-latest {{number_of_snapshots_to_keep}} --compression {{compression_algorithm}}`

- Անտեսեք հատուկ ֆայլ կամ թղթապանակ կրկնօրինակներից.:

`kopia policy set --global --add-ignore {{path/to/file_or_folder}}`
