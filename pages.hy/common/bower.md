# bower

> Փաթեթների կառավարիչ, որը օպտիմիզացված է ճակատային վեբ զարգացման համար:.
> Փաթեթը կարող է լինել GitHub օգտվող/ռեպո սղագրություն, Git վերջնակետ, URL կամ գրանցված փաթեթ:.
> Լրացուցիչ տեղեկություններ. <https://bower.io/#getting-started>:.

- Տեղադրեք նախագծի կախվածությունները, որոնք նշված են `bower.json`-ում.:

`bower install`

- Տեղադրեք մեկ կամ մի քանի փաթեթ bower_components գրացուցակում.:

`bower install {{package1 package2 ...}}`

- Տեղակայեք փաթեթները bower_components գրացուցակից.:

`bower uninstall {{package1 package2 ...}}`

- Թվարկեք տեղական փաթեթները և հնարավոր թարմացումները.:

`bower list`

- Ստեղծեք `bower.json` ֆայլ ձեր փաթեթի համար.:

`bower init`

- Տեղադրեք հատուկ կախվածության տարբերակ և ավելացրեք այն `bower.json`-ին:

`bower install {{local_name}}={{package}}#{{version}} --save`

- Ցուցադրել օգնություն կոնկրետ հրամանի համար.:

`bower help {{command}}`
