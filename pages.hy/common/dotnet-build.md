# dotnet կառուցում

> Ստեղծում է .NET հավելված և դրա կախվածությունները:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/dotnet/core/tools/dotnet-build>:.

- Կազմեք նախագիծը կամ լուծումը ընթացիկ գրացուցակում.:

`dotnet build`

- Կազմել .NET նախագիծ կամ լուծում վրիպազերծման ռեժիմում.:

`dotnet build {{path/to/project_or_solution}}`

- Կազմել թողարկման ռեժիմում.:

`dotnet build {{[-c|--configuration]}} {{Release}}`

- Կազմել առանց կախվածությունները վերականգնելու.:

`dotnet build --no-restore`

- Կազմել հատուկ խոսակցական մակարդակով.:

`dotnet build {{[-v|--verbosity]}} {{quiet|minimal|normal|detailed|diagnostic}}`

- Կազմել կոնկրետ գործարկման ժամանակի համար.:

`dotnet build {{[-r|--runtime]}} {{runtime_identifier}}`

- Նշեք ելքային գրացուցակը.:

`dotnet build {{[-o|--output]}} {{path/to/directory}}`
