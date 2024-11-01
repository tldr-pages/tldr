# dotnet add package

> 프로젝트 파일에 .NET 패키지 참조 추가 또는 업데이트.
> 더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-add-package>.

- 현재 디렉토리의 프로젝트에 패키지 추가:

`dotnet add package {{패키지}}`

- 특정 프로젝트에 패키지 추가:

`dotnet add {{경로/대상/파일.csproj}} package {{패키지}}`

- 특정 버전의 패키지를 프로젝트에 추가:

`dotnet add package {{패키지}} --version {{1.0.0}}`

- 특정 NuGet 소스를 사용하여 패키지 추가:

`dotnet add package {{패키지}} --source {{https://api.nuget.org/v3/index.json}}`

- 특정 프레임워크를 대상으로 할 때만 패키지 추가:

`dotnet add package {{패키지}} --framework {{net7.0}}`

- 패키지를 복원할 디렉토리 지정 후 추가 (`~/.nuget/packages` 기본값):

`dotnet add package {{패키지}} --package-directory {{경로/대상/폴더}}`
