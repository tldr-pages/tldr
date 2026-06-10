#մոնգոշ

> Նոր պատյան MongoDB-ի համար, փոխարինում `mongo`-ին:.
> Նշում. կապի բոլոր տարբերակները կարող են փոխարինվել մեկ տողով՝ `mongodb://user@host:port/db_name?authSource=authdb_name`:.
> Լրացուցիչ տեղեկություններ. <https://www.mongodb.com/docs/mongodb-shell/>:.

- Միացեք տեղական տվյալների բազայի լռելյայն միացքի վրա (`mongodb://localhost:27017`):

`mongosh`

- Միացեք տվյալների շտեմարանին.:

`mongosh --host {{host}} --port {{port}} {{db_name}}`

- Նույնականացրեք՝ օգտագործելով նշված օգտանունը նշված տվյալների բազայում (ձեզ կառաջարկվի գաղտնաբառ).:

`mongosh --host {{host}} --port {{port}} --username {{username}} --authenticationDatabase {{authdb_name}} {{db_name}}`

- Գնահատեք JavaScript արտահայտությունը տվյալների բազայում.:

`mongosh --eval '{{JSON.stringify(db.foo.findOne())}}' {{db_name}}`
