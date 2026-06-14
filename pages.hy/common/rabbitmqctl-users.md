# rabbitmqctl-օգտատերեր

> Կառավարեք RabbitMQ օգտվողներին, նրանց թույլտվությունները և պիտակները:.
> Լրացուցիչ տեղեկություններ. <https://www.rabbitmq.com/docs/management>:.

- Նշեք բոլոր օգտվողներին.:

`rabbitmqctl list_users`

- Ավելացնել նոր օգտվող գաղտնաբառով.:

`rabbitmqctl add_user {{username}} {{password}}`

- Ջնջել գոյություն ունեցող օգտվողին.:

`rabbitmqctl delete_user {{username}}`

- Փոխել գաղտնաբառը օգտվողի համար.:

`rabbitmqctl change_password {{username}} {{new_password}}`

- Սահմանեք թույլտվություններ օգտվողի համար կոնկրետ վիրտուալ հոսթի վրա.:

`rabbitmqctl set_permissions {{[-p|--vhost]}} {{vhost}} {{username}} {{read}} {{write}} {{configure}}`

- Մաքրել բոլոր թույլտվությունները օգտվողի համար հատուկ վիրտուալ հոսթի վրա.:

`rabbitmqctl clear_permissions {{[-p|--vhost]}} {{vhost}} {{username}}`

- Մեկ կամ մի քանի պիտակներ (օրինակ՝ ադմինիստրատոր) նշանակեք օգտվողին.:

`rabbitmqctl set_user_tags {{username}} {{tag1 tag2 ...}}`
