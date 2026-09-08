# pulumi env

> Pulumi 환경 관리.
> 더 많은 정보: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_env/>.

- 모든 환경 목록 표시:

`pulumi env ls`

- 환경 생성:

`pulumi env init {{환경_이름}}`

- 환경에 값 설정:

`pulumi env set {{환경_이름}} {{키}} {{값}}`

- 환경 정의 편집:

`pulumi env edit {{환경_이름}}`

- 환경에서 지정한 값 삭제:

`pulumi env rm {{환경_이름}} {{키}}`

- 환경 전체 삭제:

`pulumi env rm {{환경_이름}}`

- 도움말 표시:

`pulumi env {{[-h|--help]}}`
