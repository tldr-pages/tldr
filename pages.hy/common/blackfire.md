#սև կրակ

> Դիտեք, պրոֆիլ և փորձարկեք PHP հավելվածը:.
> Լրացուցիչ տեղեկություններ. <https://www.blackfire.io/>:.

- Նախաձեռնեք և կազմաձևեք Blackfire հաճախորդը.:

`blackfire config`

- Գործարկեք Blackfire գործակալը.:

`blackfire agent`

- Գործարկեք Blackfire գործակալը կոնկրետ վարդակից.:

`blackfire agent --socket="{{tcp://127.0.0.1:8307}}"`

- Գործարկեք պրոֆիլը հատուկ ծրագրի վրա.:

`blackfire run {{php path/to/file.php}}`

- Գործարկեք պրոֆիլը և հավաքեք 10 նմուշ.:

`blackfire --samples 10 run {{php path/to/file.php}}`

- Գործարկեք պրոֆիլը և թողարկեք արդյունքները որպես JSON:

`blackfire --json run {{php path/to/file.php}}`

- Վերբեռնեք պրոֆիլավորող ֆայլ Blackfire վեբ ծառայության մեջ.:

`blackfire upload {{path/to/file}}`

- Դիտեք պրոֆիլների կարգավիճակը Blackfire վեբ ծառայության վրա.:

`blackfire status`
