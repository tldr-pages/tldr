# ստեղծել օգտվող

> Ստեղծեք PostgreSQL օգտվող (դեր):.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-createuser.html>:.

- Ստեղծեք օգտատեր ինտերակտիվ կերպով.:

`createuser --interactive {{username}}`

- Ստեղծեք օգտատեր առանց հատուկ իրավունքների.:

`createuser {{username}}`

- Ստեղծեք գերօգտագործող.:

`createuser {{[-s|--superuser]}} {{username}}`

- Ստեղծեք օգտատեր, որը թույլ է տալիս ստեղծել տվյալների բազաներ, կառավարել դերերը և գաղտնաբառ պահանջել.:

`createuser {{[-d|--createdb]}} {{[-r|--createrole]}} {{[-P|--pwprompt]}} {{username}}`

- Ստեղծեք օգտատեր առանց տվյալների բազաներ ստեղծելու կամ դերեր կառավարելու հնարավորության.:

`createuser {{[-D|--no-createdb]}} {{[-R|--no-createrole]}} {{username}}`
