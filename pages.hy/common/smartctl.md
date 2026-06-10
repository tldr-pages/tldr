# smartctl

> Դիտեք սկավառակի առողջությունը, ներառյալ SMART տվյալները:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/smartctl>:.

- Ցուցադրել SMART առողջության ամփոփագիրը.:

`sudo smartctl {{[-H|--health]}} {{/dev/sdX}}`

- Ցուցադրել սարքի տեղեկատվությունը.:

`sudo smartctl {{[-i|--info]}} {{/dev/sdX}}`

- Սկսեք կարճ/երկար ինքնափորձարկում ֆոնին.:

`sudo smartctl {{[-t|--test]}} {{short|long}} {{/dev/sdX}}`

- Ցուցադրել ինքնափորձարկման մատյան.:

`sudo smartctl {{[-l|--log]}} selftest`

- Ցուցադրել ընթացիկ/վերջին ինքնափորձարկման կարգավիճակը և այլ SMART հնարավորությունները.:

`sudo smartctl {{[-c|--capabilities]}} {{/dev/sdX}}`

- Ցուցադրել սպառիչ SMART տվյալները.:

`sudo smartctl {{[-a|--all]}} {{/dev/sdX}}`
