# func

> Azure Functions 핵심 도구: Azure Functions를 로컬에서 개발하고 테스트.
> 로컬 함수는 라이브 Azure 서비스에 연결할 수 있고, Azure 구독에 함수 앱을 배포할 수 있음.
> 더 많은 정보: <https://learn.microsoft.com/azure/azure-functions/functions-run-local>.

- 새로운 함수 프로젝트를 생성:

`func init {{project}}`

- 새로운 함수 생성:

`func new`

- 로컬에서 함수 실행:

`func start`

- Azure의 함수 앱에 코드를 게시:

`func azure functionapp publish {{함수}}`

- 기존 함수 앱에서 모든 설정을 다운로드:

`func azure functionapp fetch-app-settings {{함수}}`

- 특정 스토리지 계정에 대한 연결 문자열을 가져옴:

`func azure storage fetch-connection-string {{스토리지_계정}}`
