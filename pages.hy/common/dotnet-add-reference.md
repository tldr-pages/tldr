# dotnet ավելացնել հղում

> Ավելացրեք .NET նախագիծ-նախագիծ հղումներ:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/dotnet/core/tools/dotnet-add-reference>:.

- Ծրագրին հղում ավելացրեք ընթացիկ գրացուցակում.:

`dotnet add reference {{path/to/reference.csproj}}`

- Ավելացրեք բազմաթիվ հղումներ նախագծին ընթացիկ գրացուցակում.:

`dotnet add reference {{path/to/reference1.csproj path/to/reference2.csproj ...}}`

- Ավելացրեք հղում կոնկրետ նախագծին.:

`dotnet add {{path/to/project.csproj}} reference {{path/to/reference.csproj}}`

- Ավելացրեք մի քանի հղումներ կոնկրետ նախագծին.:

`dotnet add {{path/to/project.csproj}} reference {{path/to/reference1.csproj path/to/reference2.csproj ...}}`
