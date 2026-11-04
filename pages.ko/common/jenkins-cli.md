# jenkins-cli

> 소프트웨어 개발 생명주기의 자동화를 지원하는 오픈소스 자동화 서버.
> 더 많은 정보: <https://www.jenkins.io/doc/>.

- jenkins CLI에 연결:

`java -jar jenkins-cli.jar -s {{jenkins_서버_주소}} -auth {{사용자명}}:{{api_token}}`

- jenkins 재시작:

`java -jar jenkins-cli.jar -s {{jenkins_서버_주소}} restart`

- jenkins 종료:

`java -jar jenkins-cli.jar -s {{jenkins_서버_주소}} shutdown`

- 도움말 표시:

`java -jar jenkins-cli.jar -s {{jenkins_서버_주소}} help`

- 버전 정보 표시:

`java -jar jenkins-cli.jar -s {{jenkins_서버_주소}} version`
