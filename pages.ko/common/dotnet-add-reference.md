# dotnet add reference

> .NET 프로젝트 간 참조 추가.
> 더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-add-reference>.

- 현재 디렉터리에 있는 프로젝트에 참조 추가:

`dotnet add reference {{경로/대상/참조.csproj}}`

- 현재 디렉터리에 있는 프로젝트에 여러 참조 추가:

`dotnet add reference {{경로/대상/참조1.csproj 경로/대상/참조2.csproj ...}}`

- 특정 프로젝트에 참조 추가:

`dotnet add {{경로/대상/프로젝트.csproj}} reference {{경로/대상/참조.csproj}}`

- 특정 프로젝트에 여러 참조 추가:

`dotnet add {{경로/대상/프로젝트.csproj}} reference {{경로/대상/참조1.csproj 경로/대상/참조2.csproj ...}}`
