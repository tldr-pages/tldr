# dotnet ավելացնել փաթեթ

> Ծրագրի ֆայլում ավելացրեք կամ թարմացրեք .NET փաթեթի հղումը:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/dotnet/core/tools/dotnet-add-package>:.

- Ծրագրին փաթեթ ավելացրեք ընթացիկ գրացուցակում.:

`dotnet add package {{package}}`

- Ավելացնել փաթեթ կոնկրետ նախագծին.:

`dotnet add {{path/to/file.csproj}} package {{package}}`

- Ծրագրին ավելացրեք փաթեթի որոշակի տարբերակ.:

`dotnet add package {{package}} {{[-v|--version]}} {{1.0.0}}`

- Ավելացնել փաթեթ՝ օգտագործելով հատուկ NuGet աղբյուրը.:

`dotnet add package {{package}} {{[-s|--source]}} {{https://api.nuget.org/v3/index.json}}`

- Փաթեթ ավելացրեք միայն կոնկրետ շրջանակը թիրախավորելիս.:

`dotnet add package {{package}} {{[-f|--framework]}} {{net7.0}}`

- Ավելացրեք և նշեք այն գրացուցակը, որտեղ կարելի է վերականգնել փաթեթները (`~/.nuget/packages` ըստ լռելյայն):

`dotnet add package {{package}} --package-directory {{path/to/directory}}`
