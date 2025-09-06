# dotnet restore

> .NET 프로젝트의 의존성과 도구를 복원합니다.
> 더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-restore>.

- 현재 디렉터리의 .NET 프로젝트 또는 솔루션의 의존성 복원:

`dotnet restore`

- 특정 위치의 .NET 프로젝트 또는 솔루션의 의존성 복원:

`dotnet restore {{경로/대상/프로젝트_또는_솔루션}}`

- HTTP 요청을 캐시하지 않고 의존성 복원:

`dotnet restore --no-cache`

- 마지막 복원이 성공했더라도 모든 의존성을 강제로 해결:

`dotnet restore --force`

- 패키지 소스 실패를 경고로 처리하여 의존성 복원:

`dotnet restore --ignore-failed-sources`

- 특정 상세 수준으로 의존성 복원:

`dotnet restore --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`
