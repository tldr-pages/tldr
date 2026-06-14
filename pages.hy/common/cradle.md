#օրորոց

> Cradle PHP շրջանակը:.
> Որոշ ենթահրամաններ, ինչպիսիք են `install`-ը և `package`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html>:.

- Տեղադրեք Cradle բաղադրիչները (հուշում է լրացուցիչ տեղեկությունների համար).:

`cradle install`

- Ստիպել տեղադրել և վերագրանցել ֆայլերը.:

`cradle install {{[-f|--force]}}`

- Միացեք հեռավոր սերվերին (տես `config/deploy.php`):

`cradle connect {{server_name}}`

- Ցուցադրել Cradle-ի ընթացիկ կոնֆիգուրացիան.:

`cradle config show`

- Տեղադրեք փաթեթ ընթացիկ Cradle օրինակում.:

`cradle package install {{package_name}}`

- Տեղադրված փաթեթների ցանկ.:

`cradle package list`

- Ցուցադրել օգնությունը.:

`cradle help`

- Ցուցադրման տարբերակը:

`cradle --version`
