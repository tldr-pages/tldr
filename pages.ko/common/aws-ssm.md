# aws ssm

> AWS 리소스를 안전하게 상호작용하고 관리.
> 참고: 대화형 세션을 사용하려면 Session Manager 플러그인이 설치되어 있어야 함.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/ssm/>.

- 인스턴스에서 명령 실행:

`aws ssm send-command --instance-ids {{인스턴스_아이디1 인스턴스_아이디2 ...}} --document-name "AWS-RunShellScript" --parameters 'commands=["{{명령어}}"]'`

- 인스턴스에서 실행된 명령 호출 내역 확인:

`aws ssm list-command-invocations --instance-id "{{인스턴스_아이디}}"`

- 특정 명령 호출의 출력 결과 확인:

`aws ssm list-command-invocations --command-id "{{명령어_아이디}}" --details`

- 인스턴스와 대화형 세션을 시작:

`aws ssm start-session --target "{{인스턴스_아이디}}"`

- 원격 호스트로 포트 포워딩 세션 시작:

`aws ssm start-session --target "{{인스턴스_아이디}}" --document-name "AWS-StartPortForwardingSessionToRemoteHost" --parameters '{"portNumber":["{{원격_포트}}"],"localPortNumber":["{{로컬_포트}}"]}'`
