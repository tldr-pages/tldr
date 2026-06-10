# բանկա

> Java հավելվածների/գրադարանների փաթեթավորող:.
> Լրացուցիչ տեղեկություններ. <https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>:.

- Ընթացիկ գրացուցակի բոլոր ֆայլերը ռեկուրսիվ կերպով արխիվացրեք `.jar` ֆայլում՝:

`jar cf {{file.jar}} *`

- Unzip `.jar`/`.war` ֆայլը ընթացիկ գրացուցակում.:

`jar -xvf {{file.jar}}`

- Նշեք `.jar`/`.war` ֆայլի բովանդակությունը.:

`jar tf {{path/to/file.jar}}`

- Թվարկեք `.jar`/`.war` ֆայլի բովանդակությունը՝ մանրամասն ելքով.:

`jar tvf {{path/to/file.jar}}`
