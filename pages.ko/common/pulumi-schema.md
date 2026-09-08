# pulumi schema

> Pulumi 패키지 스키마에 오류가 있는지 검사.
> 스키마 참조: <https://www.pulumi.com/docs/iac/extending-pulumi/schema/>.
> 더 많은 정보: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_schema/>.

- 패키지 스키마 점검:

`pulumi schema check {{경로/대상/파일}}`

- 타입에 대한 참조가 누락되어 있어도 실패로 처리하지 않고 패키지 스키마 검사:

`pulumi schema check --allow-dangling-references {{경로/대상/파일}}`

- 도움말 표시:

`pulumi schema check {{[-h|--help]}}`
