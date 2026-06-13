# ibmcloud iam

> 리소스에 대한 사용자 식별 및 접근 권한 관리.
> 더 많은 정보: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_commands_iam>.

- 계정의 서비스 ID 목록 표시:

`ibmcloud iam service-ids`

- 특정 서비스 ID의 모든 API 키 목록 표시:

`ibmcloud iam service-api-keys {{서비스_아이디}}`

- 설명을 포함해 서비스 ID용 API 키 생성 (확인 없이 강제로 생성):

`ibmcloud iam service-api-key-create {{api_키_이름}} {{서비스_아이디}} {{[-d|--description]}} {{설명}} {{[-f|--force]}}`

- 이 명령에서 사용 가능한 모든 작업 목록 표시:

`ibmcloud iam help`
