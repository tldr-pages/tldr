# arthas

> Java ախտորոշիչ գործիք:.
> Տես նաև՝ `arthas-watch`, `arthas-trace`:.
> Մանրամասն՝ <https://arthas.aliyun.com/en/>:.

- Սկսեք Arthas:

`java -jar {{path/to/arthas-boot.jar}}`

- Վերամիացրեք Arthas-ը (Արտասի կողմից օգտագործվող լռելյայն պորտը 3658 է).:

`telnet localhost {{port_number}}`

- Դուրս եկեք Arthas-ի ընթացիկ հաճախորդից՝ չազդելով այլ հաճախորդների վրա: հավասար է `exit`、`logout`、`q` հրաման.:

`{{exit|quit|logout|q}}`

- Դադարեցրեք Arthas սերվերը, այս սերվերին միացող Arthas-ի բոլոր հաճախորդները կանջատվեն.:

`stop`
