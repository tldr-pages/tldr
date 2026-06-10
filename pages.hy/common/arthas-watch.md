# arthas-ժամացույց

> Մեթոդ կանչել տվյալների դիտարկումը:.
> Տես նաև՝ `arthas`, `arthas-trace`:.
> Լրացուցիչ տեղեկություններ. <https://arthas.aliyun.com/en/doc/watch.html>:.

- Դիտեք մեթոդի առաջին պարամետրը և վերադարձի արժեքը և ընդլայնեք օբյեկտի ներկառուցված ատրիբուտները մինչև 4 մակարդակ.:

`watch {{class-pattern}} {{method-pattern}} '{{{ params[0],returnObj }}}' -x 4`

- Երբ մեթոդի առաջին պարամետրի արժեքը 5 է, երկրորդ պարամետրը և վերադարձի արժեքը դուրս են գալիս, իսկ օբյեկտը ընդլայնվում է 4 շերտով.:

`watch {{class-pattern}} {{method-pattern}} '{{{ params[1],returnObj }}}' '{{"5".equals(params[0])}}' -x 4`

- Երբ մեթոդը վերադառնում է կամ բացառություն է լինում, դիտարկեք երկրորդ պարամետրի count հատկությունը.:

`watch {{class-pattern}} {{method-pattern}} '{{{ params[1].count }}}' -e -s`
