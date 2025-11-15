# aws configure

> AWS CLI 환경 설정 관리.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- AWS CLI를 대화형으로 구성 (새로운 환경을 설정하거나 기본값을 업데이트):

`aws configure`

- 대화형으로 AWS CLI에 대한 명명된 프로필을 구성 (새 프로필을 생성하거나, 기존 프로필을 업데이트):

`aws configure --profile {{프로파일_이름}}`

- 특정 환경 변수의 값을 표시:

`aws configure get {{이름}}`

- 특정 프로필의 환경 변수 값을 표시:

`aws configure get {{이름}} --profile {{프로파일_이름}}`

- 특정 환경 변수의 값을 설정:

`aws configure set {{이름}} {{값}}`

- 특정 프로필의 환경 변수 값 설정:

`aws configure set {{이름}} {{값}} --profile {{프로파일_이름}}`

- 구성 파일의 항목을 나열:

`aws configure list`

- 특정 프로필에 대한 환경 설정 항목 나열:

`aws configure list --profile {{프로파일_이름}}`
