# dotnet գործարկում

> Գործարկեք .NET հավելված առանց բացահայտ կոմպիլյացիայի կամ գործարկման հրամանների:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/dotnet/core/tools/dotnet-run>:.

- Գործարկեք նախագիծը ընթացիկ գրացուցակում.:

`dotnet run`

- Գործարկել կոնկրետ նախագիծ.:

`dotnet run --project {{path/to/file.csproj}}`

- Գործարկել նախագիծը կոնկրետ փաստարկներով.:

`dotnet run -- {{arg1=foo arg2=bar ...}}`

- Գործարկեք նախագիծը՝ օգտագործելով թիրախային շրջանակի անվանումը.:

`dotnet run {{[-f|--framework]}} {{net7.0}}`

- Նշեք ճարտարապետությունը և ՕՀ-ը, որոնք հասանելի են .NET 6-ից (Մի օգտագործեք `--runtime` այս ընտրանքներով):

`dotnet run {{[-a|--arch]}} {{x86|x64|arm|arm64}} --os {{win|win7|osx|linux|ios|android}}`
