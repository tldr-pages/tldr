#քմ

> AWS Simple Queue Service հաճախորդ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/yongfei25/sqsc>:.

- Նշեք բոլոր հերթերը.:

`sqsc lq {{queue_prefix}}`

- Թվարկեք բոլոր հաղորդագրությունները հերթում.:

`sqsc ls {{queue_name}}`

- Պատճենեք բոլոր հաղորդագրությունները մեկ հերթից մյուսը.:

`sqsc cp {{source_queue}} {{destination_queue}}`

- Տեղափոխեք բոլոր հաղորդագրությունները մեկ հերթից մյուսը.:

`sqsc mv {{source_queue}} {{destination_queue}}`

- Նկարագրեք հերթ.:

`sqsc describe {{queue_name}}`

- Հարցրեք հերթ SQL շարահյուսությամբ.:

`sqsc query "SELECT body FROM {{queue_name}} WHERE body LIKE '%user%'"`

- Քաշեք բոլոր հաղորդագրությունները հերթից դեպի տեղական SQLite տվյալների բազա ձեր ներկայիս աշխատանքային գրացուցակում.:

`sqsc pull {{queue_name}}`
