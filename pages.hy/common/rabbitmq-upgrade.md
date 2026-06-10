# rabbitmq-թարմացում

> Կառավարեք RabbitMQ հանգույցի արդիականացումը:.
> Լրացուցիչ տեղեկություններ. <https://www.rabbitmq.com/docs/man/rabbitmq-upgrade.8>:.

- Սպասեք, որ քվորումի բոլոր հերթերը ունենան վերը նշված նվազագույն առցանց քվորում.:

`rabbitmq-upgrade await_online_quorum_plus_one`

- Տեղադրեք հանգույցը սպասարկման ռեժիմում.:

`rabbitmq-upgrade drain`

- Հանգույցը դուրս բերեք սպասարկումից և սովորական աշխատանքային ռեժիմի մեջ.:

`rabbitmq-upgrade revive`

- Գործարկել հետթարմացման առաջադրանքները.:

`rabbitmq-upgrade post_upgrade`

- Ցուցադրել օգնությունը.:

`rabbitmq-upgrade help`
