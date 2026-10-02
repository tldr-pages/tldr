# pulumi state

> 현재 스택의 상태를 편집.
> 더 많은 정보: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_state/>.

- 현재 스택의 상태에서 리소스 삭제:

`pulumi state delete`

- 현재 스택의 리소스를 다른 스택으로 이동:

`pulumi state move {{리소스_urn}} --dest {{스택_이름}}`

- 현재 스택의 상태에서 리소스 이름 변경:

`pulumi state rename`

- 유효하지 않은 상태 복구:

`pulumi state repair`

- `$EDITOR` 환경 변수에 지정된 편집기로 스택의 상태 편집:

`pulumi state edit --stack {{스택_이름}}`

- 도움말 표시:

`pulumi state {{[-h|--help]}}`
