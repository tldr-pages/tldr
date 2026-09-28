# pulumi new

> 새로운 Pulumi 프로젝트 생성.
> 더 많은 정보: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_new/>.

- 대화형으로 템플릿 선택:

`pulumi new`

- 지정한 템플릿 (예: `azure-python`)으로 프로젝트 생성:

`pulumi new {{제공된_템플릿}}`

- 로컬 템플릿에서 프로젝트 생성:

`pulumi new {{경로/대상/템플릿/aws-typescript}}`

- Git 저장소의 템플릿으로 프로젝트 생성:

`pulumi new {{주소}}`

- <pulumi.com> 백엔드에서 지정한 비밀값 프로바이더 사용:

`pulumi new --secrets-provider {{비밀값}}`
