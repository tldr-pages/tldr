# rabbitmq-streams

> Կառավարեք RabbitMQ հոսքերը:.
> Լրացուցիչ տեղեկություններ. <https://www.rabbitmq.com/docs/man/rabbitmq-streams.8>:.

- Նշված հանգույցում ավելացրեք հոսքի կրկնօրինակ.:

`rabbitmq-streams add_replica {{stream}} {{node}}`

- Ջնջել հոսքի կրկնօրինակը նշված հանգույցում.:

`rabbitmq-streams delete_replica {{stream}} {{node}}`

- Ցուցադրել հոսքի կարգավիճակը.:

`rabbitmq-streams stream_status {{stream}}`

- Վերագործարկեք հոսքը.:

`rabbitmq-streams restart_stream {{stream}}`

- Ցուցակ հոսքային կապեր.:

`rabbitmq-streams list_stream_connections`

- Նշեք հոսքի բոլոր սպառողներին.:

`rabbitmq-streams list_stream_consumers`

- Թվարկեք բոլոր հոսքային հրատարակիչներին.:

`rabbitmq-streams list_stream_publishers`

- Ցուցակեք հոսքի համար հետևելու տեղեկատվությունը.:

`rabbitmq-streams list_stream_tracking {{stream}}`
