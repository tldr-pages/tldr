# ibmcloud login

> IBM Cloud에 로그인하심.
> 더 많은 정보: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login>.

- 대화형 프롬프트를 사용하여 로그인:

`ibmcloud login`

- 특정 API 엔드포인트에 로그인 (기본값은 `cloud.ibm.com`):

`ibmcloud login -a {{api_엔드포인트}}`

- 사용자명, 비밀번호 및 대상 지역을 매개변수로 제공하여 로그인:

`ibmcloud login -u {{사용자명}} -p {{비밀번호}} -r {{us-south}}`

- API 키로 로그인하고, 이를 인수로 전달:

`ibmcloud login --apikey {{api_키_문자열}}`

- API 키로 로그인하여, 파일로 전달:

`ibmcloud login --apikey @{{경로/대상/api_키_파일}}`

- 연합 ID로 로그인 (single sign-on):

`ibmcloud login --sso`
