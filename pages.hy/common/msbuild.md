# msbuild

> Microsoft-ի կառուցման գործիք Visual Studio նախագծային լուծումների համար:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/visualstudio/msbuild>:.

- Կառուցեք ծրագրի առաջին ֆայլը ընթացիկ գրացուցակում.:

`msbuild`

- Ստեղծեք կոնկրետ նախագծի ֆայլ.:

`msbuild {{path/to/project_file}}`

- Նշեք մեկ կամ մի քանի կետ-ստորակետով առանձնացված թիրախներ կառուցելու համար.:

`msbuild {{path/to/project_file}} /target:{{targets}}`

- Նշեք մեկ կամ մի քանի կետով բաժանված հատկություններ.:

`msbuild {{path/to/project_file}} /property:{{name=value}}`

- Նշեք կառուցման գործիքների տարբերակը օգտագործելու համար.:

`msbuild {{path/to/project_file}} /toolsversion:{{version}}`

- Ցուցադրել մանրամասն տեղեկատվություն գրանցամատյանի վերջում այն մասին, թե ինչպես է կազմաձևվել նախագիծը.:

`msbuild {{path/to/project_file}} /detailedsummary`

- Ցուցադրել օգնությունը.:

`msbuild /help`
