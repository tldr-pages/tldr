# pulumi plugin

> 언어 및 리소스 provider 플러그인을 수동으로 관리.
> 일반적으로 이러한 플러그인을 자동으로 관리.
> 더 많은 정보: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_plugin/>.

- 다운로드된 캐시에 있는 모든 플러그인 목록 표시:

`pulumi plugin ls`

- 현재 프로젝트에서 사용하는 플러그인 목록을 JSON 형식으로 표시:

`pulumi plugin {{[-p|--project]}} {{[-j|--json]}}`

- 지정한 종류 (예: resource)의 플러그인을 최신 버전 또는 특정 버전으로 설치:

`pulumi plugin install {{종류}} {{이름}} {{버전}}`

- 지정한 종류의 플러그인을 제거 (예: 리소스) (버전을 대화형으로 선택 또는 직접 지정):

`pulumi plugin rm {{종류}} {{이름}} {{버전}}`

- 도움말 표시:

`pulumi plugin {{[-h|--help]}}`
