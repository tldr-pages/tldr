# cf

> Cloud Foundry에서 앱과 서비스를 관리.
> 더 많은 정보: <https://docs.cloudfoundry.org/cf-cli/getting-started.html>.

- Cloud Foundry API에 로그인:

`cf login -a {{api_주소}}`

- 기본 설정을 사용하여 앱을 푸시:

`cf push {{앱_이름}}`

- 조직에서 사용할 수 있는 서비스 보기:

`cf marketplace`

- 서비스 인스턴스를 생성:

`cf create-service {{서비스}} {{플랜}} {{서비스_이름}}`

- 애플리케이션을 서비스에 연결:

`cf bind-service {{앱_이름}} {{서비스_이름}}`

- 코드가 앱에 포함되어 있지만, 독립적으로 실행되는 스크립트를 실행:

`cf run-task {{앱_이름}} "{{스크립트_명령어}}" --name {{작업_이름}}`

- 앱을 호스팅하는 VM으로 대화형 SSH 세션을 시작:

`cf ssh {{앱_이름}}`

- 최근 앱 로그 덤프 보기:

`cf logs {{앱_이름}} --recent`
