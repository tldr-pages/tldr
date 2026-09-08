# pulumi stack history

> 스택의 변경 이력을 표시.
> 더 많은 정보: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_stack_history/>.

- 현재 스택의 변경 이력 표시:

`pulumi stack {{[hist|history]}}`

- 상대 날짜 대신 전체 날짜를 사용하여 현재 스택의 변경 이력 표시:

`pulumi stack {{[hist|history]}} --full-dates`

- 현재 스택의 변경이력을 JSON 형식으로 표시:

`pulumi stack {{[hist|history]}} {{[-j|--json]}}`

- 지정한 스택의 변경 이력 표시:

`pulumi stack {{[hist|history]}} {{[-s|--stack]}} {{스택_이름}}`

- 도움말 표시:

`pulumi stack {{[hist|history]}} {{[-h|--help]}}`
