# մինիո սերվեր

> MinIO սերվերի հրաման՝ MinIO S3 համատեղելի պահեստավորման շարժիչը գործարկելու համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.min.io/enterprise/aistor-object-store/reference/aistor-server/>:.

- Սկսեք սերվեր՝ օգտագործելով լռելյայն կոնֆիգուրացիան.:

`minio server {{path/to/data_directory}}`

- Սկսեք սերվեր, որը կապում է API-ի և վեբ կոնսոլի այլ նավահանգիստին.:

`minio server --address ":{{port}}" --console-address ":{{port}}" {{path/to/data_directory}}`

- Սկսեք սերվերը որպես 2 հանգույցների կլաստերի մի մաս.:

`minio server {{node1_hostname}} {{path/to/data_directory}} {{node2_hostname}} {{path/to/data_directory}}`
