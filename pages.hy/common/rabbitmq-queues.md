# rabbitmq-հերթեր

> Կառավարեք RabbitMQ հերթերը:.
> Լրացուցիչ տեղեկություններ. <https://www.rabbitmq.com/docs/man/rabbitmq-queues.8>:.

- Աճեք քվորումի հերթերի կլաստերները՝ ավելացնելով անդամ նշված հանգույցում.:

`rabbitmq-queues grow {{node}} {{all|even}}`

- Վերահավասարակշռեք կրկնվող հերթերի առաջատարները հանգույցների միջով.:

`rabbitmq-queues rebalance {{all|quorum|stream}}`

- Փոքրացնել քվորումի հերթերի կլաստերները՝ հեռացնելով նշված հանգույցի անդամներից որևէ մեկը.:

`rabbitmq-queues shrink {{node}}`

- Նշված հանգույցում ավելացրեք քվորումի հերթի անդամ.:

`rabbitmq-queues add_member {{queue}} {{node}}`

- Ջնջել քվորումի հերթի անդամը նշված հանգույցում.:

`rabbitmq-queues delete_member {{queue}} {{node}}`

- Ցուցադրել քվորումի հերթի քվորումի կարգավիճակը.:

`rabbitmq-queues quorum_status {{queue}}`
