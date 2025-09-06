# dotnet build

> .NET 애플리케이션과 그 의존성을 빌드.
> 더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-build>.

- 현재 디렉토리의 프로젝트나 솔루션 컴파일:

`dotnet build`

- 디버그 모드에서 .NET 프로젝트나 솔루션 컴파일:

`dotnet build {{경로/대상/프로젝트_또는_솔루션}}`

- 릴리즈 모드에서 컴파일:

`dotnet build --configuration {{Release}}`

- 의존성을 복원하지 않고 컴파일:

`dotnet build --no-restore`

- 특정 상세 수준으로 컴파일:

`dotnet build --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`

- 특정 런타임을 위해 컴파일:

`dotnet build --runtime {{런타임_식별자}}`

- 출력 디렉토리 지정:

`dotnet build --output {{경로/대상/폴더}}`
