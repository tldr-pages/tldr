# dotnet հրապարակում

> Հրապարակեք .NET հավելվածը և դրա կախվածությունները հոսթինգ համակարգում տեղակայման գրացուցակում:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/dotnet/core/tools/dotnet-publish>:.

- Կազմեք .NET նախագիծ թողարկման ռեժիմում.:

`dotnet publish {{[-c|--configuration]}} Release {{path/to/project_file}}`

- Հրապարակեք .NET Core գործարկման ժամանակը ձեր հավելվածի հետ նշված գործարկման ժամանակի համար.:

`dotnet publish {{[-sc|--self-contained]}} true {{[-r|--runtime]}} {{runtime_identifier}} {{path/to/project_file}}`

- Հավելվածը փաթեթավորեք պլատֆորմի համար հատուկ մեկ ֆայլ գործարկվողի մեջ.:

`dotnet publish {{[-r|--runtime]}} {{runtime_identifier}} -p:PublishSingleFile=true {{path/to/project_file}}`

- Կտրեք չօգտագործված գրադարանները՝ հավելվածի տեղակայման չափը նվազեցնելու համար.:

`dotnet publish {{[-sc|--self-contained]}} true {{[-r|--runtime]}} {{runtime_identifier}} -p:PublishTrimmed=true {{path/to/project_file}}`

- Կազմեք .NET նախագիծ՝ առանց կախվածությունը վերականգնելու.:

`dotnet publish --no-restore {{path/to/project_file}}`

- Նշեք ելքային գրացուցակը.:

`dotnet publish {{[-o|--output]}} {{path/to/directory}} {{path/to/project_file}}`
