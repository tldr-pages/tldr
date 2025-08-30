# pulumi stack

> 스택을 관리하고 스택 상태를 확인.
> 더 많은 정보: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_stack/>.

- 새 스택 생성:

`pulumi stack init {{스택_이름}}`

- 스택 상태 보기:

`pulumi stack`

- 현재 프로젝트의 스택 나열:

`pulumi stack ls`

- 모든 프로젝트의 스택 나열:

`pulumi stack ls {{[-a|--all]}}`

- 활성 스택 선택:

`pulumi stack select {{스택_이름}}`

- 스택 출력을 평문으로 표시 (비밀 포함):

`pulumi stack output --show-secrets`

- 스택 상태를 JSON 파일로 내보내기:

`pulumi stack export --file {{경로/대상/파일.json}}`

- 도움말 표시:

`pulumi stack {{[-h|--help]}}`
