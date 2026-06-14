# elasticsarch-croneval

> Վավերացրեք և գնահատեք `cron` արտահայտությունը: Այս հրամանն օգնում է ստուգել, ​​որ `cron` արտահայտությունները վավեր են Elasticsearch-ի հետ օգտագործելու համար և տալիս են ակնկալվող արդյունքները:.
> Լրացուցիչ տեղեկություններ. <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/elasticsearch-croneval>:.

- Գնահատեք `cron` արտահայտությունը և ցուցադրեք հաջորդ 10 գործարկման ժամանակները (կանխադրված վարքագիծ).:

`elasticsearch-croneval "{{cron_expression}}"`

- Գնահատեք `cron` արտահայտությունը և ցուցադրեք ապագա գործարկման ժամանակների որոշակի քանակ.:

`elasticsearch-croneval "{{cron_expression}}" {{[-c|--count]}} {{integer}}`

- Ցուցադրել մանրամասն տեղեկատվություն (ներառյալ կույտի հետքը) անվավեր `cron` արտահայտության համար.:

`elasticsearch-croneval "{{invalid_cron_expression}}" {{[-d|--detail]}}`

- Ցուցադրել նվազագույն ելքը (լուռ ռեժիմ).:

`elasticsearch-croneval "{{cron_expression}}" {{[-s|--silent]}}`

- Ցուցադրել մանրամասն ելքը.:

`elasticsearch-croneval "{{cron_expression}}" {{[-v|--verbose]}}`
