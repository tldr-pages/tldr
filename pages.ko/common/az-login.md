# az login

> Azure에 로그인.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/reference-index#az-login>.

- 대화형으로 로그인:

`az login`

- 클라이언트 암호를 사용하여 서비스 주체로 로그인:

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-service-principal}} {{[-p|--password]}} {{비밀}} {{[-t|--tenant]}} {{someone.onmicrosoft.com}}`

- 클라이언트 인증서를 사용하여 서비스 주체로 로그인:

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-service-principal}} {{[-p|--password]}} {{경로/대상/cert.pem}} {{[-t|--tenant]}} {{someone.onmicrosoft.com}}`

- VM의 시스템 할당 ID를 사용하여 로그인:

`az login {{[-i|--identity]}}`

- VM의 사용자 할당 ID를 사용하여 로그인:

`az login {{[-i|--identity]}} {{[-u|--username]}} /subscriptions/{{구독_아이디}}/resourcegroups/{{나의_리소스그룹}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{나의_아이디}}`
