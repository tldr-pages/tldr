# pulumi policy

> Pulumi Cloud (Business Critical) 또는 로컬에서 리소스 정책을 관리 (조직 관련 하위 명령 사용 불가).
> 더 많은 정보: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_policy/>.

- 템플릿 또는 URL을 사용하여 새로운 Pulumi Policy Pack을 생성:

`pulumi policy new --dir {{경로/대상/디렉터리}} {{template|url}}`

- 정책 설정의 구문 유효성 검사. 프로젝트에 정책을 적용하여 검사하려면 `pulumi preview` 사용:

`pulumi policy validate-config {{조직_이름}}/{{정책_모음_이름}} {{버전}}`

- 조직의 모든 정책 목록 표시:

`pulumi policy ls {{[-j|--json]}} {{조직_이름}}`

- 정책을 Pulumi Cloud에 게시:

`pulumi policy publish {{조직_이름}}`

- 지정한 버전의 정책 활성화:

`pulumi policy enable {{조직_이름}}/{{정책_모음_이름}} {{latest|버전}}`

- 지정한 버전의 정책 비활성화 (기본값: 모든 버전):

`pulumi policy disable {{조직_이름}}/{{정책_모음_이름}} --version {{버전}}`

- 도움말 표시:

`pulumi policy {{[-h|--help]}}`
