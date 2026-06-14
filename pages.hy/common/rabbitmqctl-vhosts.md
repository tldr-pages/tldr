# rabbitmqctl-vhosts

> Կառավարեք վիրտուալ հոստեր (vhosts) RabbitMQ-ում:.
> Vhost-ներն օգտագործվում են մի քանի տրամաբանական բրոքերների առանձնացնելու համար նույն RabbitMQ սերվերում:.
> Լրացուցիչ տեղեկություններ. <https://www.rabbitmq.com/docs/vhosts>:.

- Թվարկեք բոլոր վիրտուալ հյուրընկալողները.:

`rabbitmqctl list_vhosts`

- Ավելացնել նոր վիրտուալ հոսթ.:

`rabbitmqctl add_vhost {{vhost_name}}`

- Ջնջել վիրտուալ հոսթ.:

`rabbitmqctl delete_vhost {{vhost_name}}`

- Սահմանեք թույլտվություններ օգտվողի համար կոնկրետ վիրտուալ հոսթի վրա.:

`rabbitmqctl set_permissions {{[-p|--vhost]}} {{vhost_name}} {{username}} {{read}} {{write}} {{configure}}`

- Մաքրել թույլտվությունները որոշակի վիրտուալ հոսթի վրա օգտագործողի համար.:

`rabbitmqctl clear_permissions {{[-p|--vhost]}} {{vhost_name}} {{username}}`
