# dotnet test

> .NET 애플리케이션의 테스트를 실행.
> 참고: 지원되는 필터 표현식은 <https://learn.microsoft.com/en-us/dotnet/core/testing/selective-unit-tests>를 참조.
> 더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-test>.

- 현재 디렉토리의 .NET 프로젝트/솔루션에 대한 테스트 실행:

`dotnet test`

- 특정 위치에 있는 .NET 프로젝트/솔루션에 대한 테스트 실행:

`dotnet test {{경로/대상/프로젝트_또는_솔루션}}`

- 주어진 필터 표현식과 일치하는 테스트 실행:

`dotnet test --filter {{Name~TestMethod1}}`
