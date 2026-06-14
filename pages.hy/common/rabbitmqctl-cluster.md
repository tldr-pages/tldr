# rabbitmqctl-կլաստեր

> Կառավարեք RabbitMQ հանգույցները կլաստերի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://www.rabbitmq.com/docs/man/rabbitmqctl.8>:.

- Ցուցադրել կլաստերի կարգավիճակը.:

`rabbitmqctl cluster_status`

- Ցուցադրել ընթացիկ հանգույցի կարգավիճակը.:

`rabbitmqctl status`

- Սկսեք RabbitMQ հավելվածը որոշակի հանգույցի վրա.:

`rabbitmqctl {{[-n|--node]}} {{nodename}} start_app`

- Դադարեցրեք RabbitMQ հավելվածը կոնկրետ հանգույցի վրա.:

`rabbitmqctl {{[-n|--node]}} {{nodename}} stop_app`

- Դադարեցրեք կոնկրետ RabbitMQ հանգույց.:

`rabbitmqctl {{[-n|--node]}} {{nodename}} stop`

- Վերականգնել կոնկրետ RabbitMQ հանգույցը մաքուր վիճակի.:

`rabbitmqctl {{[-n|--node]}} {{nodename}} reset`

- Ստիպեք ընթացիկ հանգույցը միանալ գոյություն ունեցող կլաստերին.:

`rabbitmqctl join_cluster {{nodename}}`
