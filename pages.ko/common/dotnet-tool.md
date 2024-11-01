# dotnet tool

> .NET 도구를 관리하고 NuGet에서 게시된 도구를 검색.
> 더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/global-tools>.

- 전역 도구 설치 (`--global`은 로컬 도구에는 사용하지 않음):

`dotnet tool install --global {{dotnetsay}}`

- 로컬 도구 매니페스트에 정의된 도구 설치:

`dotnet tool restore`

- 특정 전역 도구 업데이트 (`--global`은 로컬 도구에는 사용하지 않음):

`dotnet tool update --global {{도구_이름}}`

- 전역 도구 제거 (`--global`은 로컬 도구에는 사용하지 않음):

`dotnet tool uninstall --global {{도구_이름}}`

- 설치된 전역 도구 나열 (`--global`은 로컬 도구에는 사용하지 않음):

`dotnet tool list --global`

- NuGet에서 도구 검색:

`dotnet tool search {{검색_어구}}`

- 도움말 표시:

`dotnet tool --help`
