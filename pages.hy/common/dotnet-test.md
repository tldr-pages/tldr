# dotnet թեստ

> Կատարեք թեստեր .NET հավելվածի համար:.
> Նշում. դիտեք <https://learn.microsoft.com/dotnet/core/testing/selective-unit-tests> աջակցվող ֆիլտրի արտահայտությունները:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/dotnet/core/tools/dotnet-test>:.

- Կատարեք թեստեր .NET նախագծի/լուծման համար ընթացիկ գրացուցակում.:

`dotnet test`

- Կատարեք թեստեր .NET նախագծի/լուծման համար որոշակի վայրում.:

`dotnet test {{path/to/project_or_solution}}`

- Կատարեք թեստեր, որոնք համապատասխանում են տվյալ ֆիլտրի արտահայտությանը.:

`dotnet test --filter {{Name~TestMethod1}}`
