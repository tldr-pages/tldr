# dotnet

> .NET Core를 위한 크로스 플랫폼 .NET 명령어 도구.
> 더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools>.

- 새 .NET 프로젝트 초기화하기:

`dotnet new {{짧은_템플릿_이름}}`

- nuget 패키지들 복구하기:

`dotnet restore`

- 현재 디렉토리에서 .NET 프로젝트를 빌드하고 실행하기:

`dotnet run`

- 패키지화 된 dotnet 어플리케이션을 실행하기(런타임만 필요하며, 나머지 명령어들은 .NET Core SDK 설치가 필요):

`dotnet {{경로/어플리케이션.dll}}`
