# aws cloudformation

> 인프라를 코드로 처리하여 AWS 및 타사 리소스를 모델링, 프로비저닝 및 관리.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html>.

- 템플릿 파일에서 스택 생성:

`aws cloudformation create-stack --stack-name {{스택-이름}} --region {{지역}} --template-body {{file://경로/대상/파일.yml}} --profile {{프로파일}}`

- 스택 삭제:

`aws cloudformation delete-stack --stack-name {{스택-이름}} --profile {{프로파일}}`

- 모든 스택 나열:

`aws cloudformation list-stacks --profile {{프로파일}}`

- 실행 중인 모든 스택 나열:

`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --profile {{프로파일}}`

- 스택 상태 확인:

`aws cloudformation describe-stacks --stack-name {{스택-아이디}} --profile {{프로파일}}`

- 스택에 대한 드리프트 감지 시작:

`aws cloudformation detect-stack-drift --stack-name {{스택-아이디}} --profile {{프로파일}}`

- 이전 명령어 호출 결과의 'StackDriftDetectionId'를 사용하여 스택의 드리프트 상태 출력을 확인:

`aws cloudformation describe-stack-resource-drifts --stack-name {{스택-드리프트-탐지-아이디}} --profile {{프로파일}}`
