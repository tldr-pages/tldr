# dotnet

> Cross platform .NET գործիքներ .NET Core-ի համար:.
> Որոշ ենթահրամաններ, ինչպիսիք են `build`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/dotnet/core/tools>:.

- Նախաձեռնեք նոր .NET նախագիծ.:

`dotnet new {{template_short_name}}`

- Վերականգնել NuGet փաթեթները.:

`dotnet restore`

- Կառուցեք և գործարկեք .NET նախագիծը ընթացիկ գրացուցակում.:

`dotnet run`

- Գործարկեք փաթեթավորված dotnet հավելված (միայն անհրաժեշտ է գործարկման ժամանակը, մնացած հրամանները պահանջում են տեղադրել .NET Core SDK):

`dotnet {{path/to/application.dll}}`
