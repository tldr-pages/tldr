# dotnet publish

> .NET 애플리케이션과 그 의존성을 호스팅 시스템에 배포하기 위해 디렉터리에 게시.
> 더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-publish>.

- .NET 프로젝트를 릴리스 모드로 컴파일:

`dotnet publish --configuration Release {{경로/대상/프로젝트_파일}}`

- 지정된 런타임에 대해 .NET Core 런타임을 애플리케이션과 함께 게시:

`dotnet publish --self-contained true --runtime {{런타임_식별자}} {{경로/대상/프로젝트_파일}}`

- 애플리케이션을 플랫폼별 단일 파일 실행 파일로 패키징:

`dotnet publish --runtime {{런타임_식별자}} -p:PublishSingleFile=true {{경로/대상/프로젝트_파일}}`

- 사용하지 않는 라이브러리를 제거하여 애플리케이션의 배포 크기 줄이기:

`dotnet publish --self-contained true --runtime {{런타임_식별자}} -p:PublishTrimmed=true {{경로/대상/프로젝트_파일}}`

- 의존성을 복원하지 않고 .NET 프로젝트 컴파일:

`dotnet publish --no-restore {{경로/대상/프로젝트_파일}}`

- 출력 디렉터리 지정:

`dotnet publish --output {{경로/대상/폴더}} {{경로/대상/프로젝트_파일}}`
