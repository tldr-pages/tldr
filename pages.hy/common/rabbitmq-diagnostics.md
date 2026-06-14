# rabbitmq-diagnostics

> Ախտորոշեք, վերահսկեք և կատարեք առողջության ստուգումներ RabbitMQ հանգույցների վրա:.
> Շատ ենթահրամաններ պատվիրակված են `rabbitmqctl`-ին:.
> Լրացուցիչ տեղեկություններ. <https://www.rabbitmq.com/docs/man/rabbitmq-diagnostics.8>:.

- Նշեք ռեսուրսների ահազանգերը.:

`rabbitmq-diagnostics alarms`

- Ցուցակել հանգույցների վկայագրերը.:

`rabbitmq-diagnostics certificates`

- Ստուգեք, արդյոք RabbitMQ-ն աշխատում է նշված հանգույցում.:

`rabbitmq-diagnostics check_running --node {{node}}`

- Գործարկել հասակակիցների բացահայտումը.:

`rabbitmq-diagnostics discover_peers`

- Ցուցակ ունկնդիրներ (կապված վարդակներ).:

`rabbitmq-diagnostics listeners`

- Տպեք վերջին `n` մատյան տողերը նշված հանգույցում.:

`rabbitmq-diagnostics log_tail --number {{n}} --node {{node}}`
