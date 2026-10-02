# pulumi import

> 기존 리소스를 pulumi 스택으로 가져옴.
> 클라우드 제공업체 별 구문: <https://www.pulumi.com/registry/>.
> 더 많은 정보: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_import/>.

- 기존 프로바이더 리소스를 지정한 이름의 Pulumi 리소스로 가져와 리소스 정의 생성:

`pulumi import {{타입_토큰}} {{이름}} {{아이디}}`

- 기존 AWS 사용자를 `pulumi` 리소스로 가져오기:

`pulumi import aws:iam/user:User {{my_user_resource}} {{id}}`

- 기존 Cloudflare worker를 pulumi 리소스로 가져오기:

`pulumi import cloudflare:index/workersScript:WorkersScript {{워커_스크립트}} {{계정_아이디/스크립트_이름}}`

- JSON 파일을 사용하여 여러 리소스를 일괄 가져오고 결과를 `stdout` 대신 파일에 저장:

`pulumi import --file {{경로/대상/파일.json}} --out {{경로/대상/파일}}`
