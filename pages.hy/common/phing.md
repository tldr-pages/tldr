#ֆինգ

> Apache Ant-ի վրա հիմնված PHP ստեղծման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://www.phing.info/guide/chunkhtml/ch03s03.html>:.

- Կատարեք կանխադրված առաջադրանքը `build.xml` ֆայլում՝:

`phing`

- Նախաձեռնեք նոր կառուցման ֆայլ.:

`phing {{[-i|--init]}} {{path/to/build.xml}}`

- Կատարել կոնկրետ առաջադրանք.:

`phing {{task_name}}`

- Օգտագործեք կառուցման ֆայլի տրված ուղին.:

`phing {{[-f|-buildfile]}} {{path/to/build.xml}} {{task_name}}`

- Մուտք գործեք տվյալ ֆայլ.:

`phing -logfile {{path/to/log_file}} {{task_name}}`

- Կառուցման մեջ օգտագործեք հատուկ հատկություններ.:

`phing -D{{property}}={{value}} {{task_name}}`

- Նշեք հատուկ լսողի դաս.:

`phing -listener {{class_name}} {{task_name}}`

- Կառուցեք՝ օգտագործելով մանրամասն ելք.:

`phing -verbose {{task_name}}`
