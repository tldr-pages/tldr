# aws-vault

> Un vault per memorizzare e accedere in modo sicuro alle credenziali AWS in ambienti di sviluppo.
> Maggiori informazioni: <https://github.com/99designs/aws-vault>.

- Aggiunge credenziali al keystore sicuro:

`aws-vault add {{profilo}}`

- Esegue un comando con credenziali AWS nell'ambiente:

`aws-vault exec {{profilo}} -- {{aws s3 ls}}`

- Apre una finestra del browser e accede alla Console AWS:

`aws-vault login {{profilo}}`

- Elenca i profili, insieme alle loro credenziali e sessioni:

`aws-vault list`

- Ruota le credenziali AWS:

`aws-vault rotate {{profilo}}`

- Rimuove le credenziali dal keystore sicuro:

`aws-vault remove {{profilo}}`
