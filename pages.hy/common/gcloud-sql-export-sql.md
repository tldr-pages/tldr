# gcloud sql արտահանման sql

> Արտահանել տվյալները Cloud SQL օրինակից Google Cloud Storage-ի SQL ֆայլ:.
> Օգտակար է կրկնօրինակներ ստեղծելու կամ տվյալներ տեղափոխելու համար:.
> Տես նաև՝ `gcloud`:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/sql>:.

- Արտահանեք տվյալները Cloud SQL-ի որոշակի օրինակից Google Cloud Storage-ի դույլ որպես SQL աղբանոց.:

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}}`

- Արտահանեք տվյալները ասինխրոն կերպով՝ անմիջապես վերադառնալով՝ առանց սպասելու գործողության ավարտին.:

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --async`

- Արտահանեք տվյալներ հատուկ տվյալների բազաներից Cloud SQL օրինակում.:

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --database={{database1,database2,...}}`

- Արտահանել հատուկ աղյուսակներ նշված տվյալների բազայից Cloud SQL օրինակում.:

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --database={{database}} --table={{table1,table2,...}}`

- Արտահանեք տվյալները՝ գործողությունը ժամանակավոր օրինակ բեռնելիս՝ աղբյուրի օրինակի վրա ճնշումը նվազեցնելու համար.:

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --offload`

- Արտահանեք տվյալները և սեղմեք ելքը `gzip`-ով.:

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}}.gz`
