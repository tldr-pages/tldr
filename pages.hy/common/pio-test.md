# pio թեստ

> Գործարկել տեղական թեստերը PlatformIO նախագծի վրա:.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/cmd_test.html>:.

- Գործարկեք բոլոր թեստերը ընթացիկ PlatformIO նախագծի բոլոր միջավայրերում.:

`pio test`

- Փորձարկեք միայն հատուկ միջավայրեր.:

`pio test {{[-e|--environment]}} {{environment1}} {{[-e|--environment]}} {{environment2}}`

- Գործարկեք միայն թեստերը, որոնց անունը համապատասխանում է որոշակի գլոբուսի օրինակին.:

`pio test {{[-f|--filter]}} "{{pattern}}"`

- Անտեսեք թեստերը, որոնց անունը համապատասխանում է որոշակի գլոբուսի օրինակին.:

`pio test {{[-i|--ignore]}} "{{pattern}}"`

- Նշեք մի նավահանգիստ որոնվածը վերբեռնելու համար.:

`pio test --upload-port {{upload_port}}`

- Նշեք հատուկ կազմաձևման ֆայլ՝ թեստերն իրականացնելու համար.:

`pio test {{[-c|--project-conf]}} {{path/to/platformio.ini}}`
