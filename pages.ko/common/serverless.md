# serverless

> AWS, Google Cloud, Azure 및 IBM OpenWhisk에서 서버리스 아키텍처를 배포하고 운영하기 위한 도구 모음.
> 명령은 `serverless` 명령어 또는 그 별칭인 `sls`를 사용하여 실행할 수 있습니다.
> 더 많은 정보: <https://www.serverless.com/framework/docs/providers/aws/cli-reference>.

- 서버리스 프로젝트 생성:

`serverless create`

- 템플릿에서 서버리스 프로젝트 생성:

`serverless create --template {{템플릿_이름}}`

- 클라우드 공급자에 배포:

`serverless deploy`

- 서버리스 프로젝트 정보 표시:

`serverless info`

- 배포된 함수 호출:

`serverless invoke -f {{함수_이름}}`

- 프로젝트의 로그를 실시간으로 추적:

`serverless logs -t`
