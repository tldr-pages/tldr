# doctl տվյալների բազաների օգտվող

> Դիտեք տվյալների բազայի օգտվողների մանրամասները և ստեղծեք դրանք:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/databases/user/>:.

- Գործարկեք `doctl databases user` հրամանը մուտքի նշանով.:

`doctl {{[d|databases]}} {{[u|user]}} {{command}} {{[-t|--access-token]}} {{access_token}}`

- Ստացեք տվյալների բազայի օգտագործողի մասին մանրամասներ.:

`doctl {{[d|databases]}} {{[u|user]}} {{[g|get]}} {{database_id}} {{user_name}}`

- Առբերեք տվյալների բազայի օգտագործողների ցուցակը տվյալ տվյալների բազայի համար.:

`doctl {{[d|databases]}} {{[u|user]}} {{[ls|list]}} {{database_id}}`

- Վերականգնել auth գաղտնաբառը տվյալ օգտվողի համար.:

`doctl {{[d|databases]}} {{[u|user]}} {{[rs|reset]}} {{database id}} {{user_name}}`

- Վերականգնել MySQL վավերացման հավելումը տվյալ օգտվողի համար.:

`doctl {{[d|databases]}} {{[u|user]}} {{[rs|reset]}} {{database_id}} {{user_name}} {{caching_sha2_password|mysql_native_password}}`

- Ստեղծեք օգտատեր տվյալ տվյալների բազայում տվյալ օգտվողի անունով.:

`doctl {{[d|databases]}} {{[u|user]}} {{[c|create]}} {{database_id}} {{user_name}}`

- Ջնջել օգտվողին տվյալ տվյալների բազայից տվյալ օգտվողի անունով.:

`doctl {{[d|databases]}} {{[u|user]}} {{[rm|delete]}} {{database_id}} {{user_name}}`
