# pulumi up

> 스택의 리소스를 생성하거나 업데이트.
> 더 많은 정보: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_up/>.

- 프로그램 및/또는 인프라에 대한 변경 사항 미리보기 및 배포:

`pulumi up`

- 미리보기 후 자동 승인 및 업데이트 수행:

`pulumi up {{[-y|--yes]}}`

- 특정 스택에서 변경 사항 미리보기 및 배포:

`pulumi up {{[-s|--stack]}} {{스택}}`

- 스택 출력을 표시하지 않음:

`pulumi up --suppress-outputs`

- 오류가 발생하더라도 리소스 업데이트 계속 진행:

`pulumi up --continue-on-error`
