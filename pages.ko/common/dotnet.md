# dotnet

> 크로스 플랫폼 .NET Core용 명령줄 도구.
> `build`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools>.

- 새 .NET 프로젝트 초기화:

`dotnet new {{템플릿_짧은_이름}}`

- NuGet 패키지 복원:

`dotnet restore`

- 현재 디렉터리에서 .NET 프로젝트를 빌드하고 실행:

`dotnet run`

- 패키지된 dotnet 애플리케이션 실행 (런타임만 필요하며, 나머지 명령은 .NET Core SDK 설치 필요):

`dotnet {{경로/대상/application.dll}}`
