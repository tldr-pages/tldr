# rekor-cli

> Անփոփոխ կեղծման դիմացկուն մետատվյալների մատյան, որը ստեղծվել է ծրագրային նախագծերի մատակարարման շղթայում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sigstore/rekor>:.

- Վերբեռնեք արտեֆակտ Rekor-ում.:

`rekor-cli upload --artifact {{path/to/file.ext}} --signature {{path/to/file.ext.sig}} --pki-format={{x509}} --public-key={{path/to/key.pub}}`

- Ստացեք տեղեկատվություն Թափանցիկության մատյանում գրառումների վերաբերյալ.:

`rekor-cli get --uuid={{0e81b4d9299e2609e45b5c453a4c0e7820ac74e02c4935a8b830d104632fd2d1}}`

- Որոնեք Rekor ինդեքսը՝ Artifact-ով գրառումներ գտնելու համար.:

`rekor-cli search --artifact {{path/to/file.ext}}`

- Որոնեք Rekor ինդեքսը՝ որոշակի հեշով գրառումներ գտնելու համար.:

`rekor-cli search --sha {{6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b}}`
