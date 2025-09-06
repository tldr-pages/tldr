# aws codeartifact

> CodeArtifact 리포지토리, 도메인, 패키지, 패키지 버전 및 자산을 관리.
> CodeArtifact는 인기 있는 패키지 관리자 및 Maven, Gradle, npm, Yarn, Twine, pip, NuGet 및 SwiftPM과 같은 빌드 도구와 호환되는 아티팩트 리포지토리.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html>.

- AWS 계정에 사용 가능한 도메인 나열:

`aws codeartifact list-domains`

- 특정 패키지 관리자에 대한 자격 증명 생성:

`aws codeartifact login --tool {{npm|pip|twine}} --domain {{_도메인}} --repository {{레포지토리_이름}}`

- CodeArtifact 레포지토리의 엔드포인트 URL 가져오기:

`aws codeartifact get-repository-endpoint --domain {{your_domain}} --repository {{레포지토리_이름}} --format {{npm|pypi|maven|nuget|generic}}`

- 도움말 표시:

`aws codeartifact help`

- 특정 하위 명령어에 대한 도움말 표시:

`aws codeartifact {{subcommand}} help`
