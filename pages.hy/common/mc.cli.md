#մկ

> MinIO Client օբյեկտների պահպանման և ֆայլային համակարգերի համար:.
> Որոշ համակարգերում կարող է անվանվել `mc` կամ `mcli`:.
> Լրացուցիչ տեղեկություններ. <https://minio.github.io/mc/>:.

- Ավելացնել կապ S3 սերվերին.:

`mc alias set {{local}} {{http://localhost:9000}} {{access_key}} {{secret_key}}`

- Ստեղծեք դույլ.:

`mc mb {{local/bucket_name}}`

- Թվարկեք դույլերը և դրանց բովանդակությունը ռեկուրսիվորեն.:

`mc ls {{local}} --recursive`
