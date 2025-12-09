# aws amplify

> 안전하고, 확장 가능한 모바일 및 웹 애플리케이션을 구축하기 위한 개발 플랫폼.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/index.html>.

- 새로운 Amplify 앱 생성:

`aws amplify create-app --name {{앱_이름}} --description {{세부정보}} --repository {{레포지토리_주소}} --platform {{플랫폼}} --environment-variables {{환경_변수}} --tags {{태그}}`

- 기존 Amplify 앱 삭제:

`aws amplify delete-app --app-id {{앱_아이디}}`

- 특정 Amplify 앱 세부정보 가져오기:

`aws amplify get-app --app-id {{앱_아이디}}`

- 모든 Amplify 앱 나열:

`aws amplify list-apps`

- Amplify 앱 설정 업데이트:

`aws amplify update-app --app-id {{앱_아이디}} --name {{새로운_이름}} --description {{새로운_세부정보}} --repository {{새로운_레포지토리_주소}} --environment-variables {{새로운_환경_변수}} --tags {{새로운_태그}}`

- Amplify 앱에 새로운 백엔드 환경 추가:

`aws amplify create-backend-environment --app-id {{앱_아이디}} --environment-name {{환경변수_이름}} --deployment-artifacts {{artifacts}}`

- Amplify 앱에서 백엔드 환경 제거:

`aws amplify delete-backend-environment --app-id {{앱_아이디}} --environment-name {{환경변수_이름}}`

- Amplify 앱의 모든 백엔드 환경 나열:

`aws amplify list-backend-environments --app-id {{앱_아이디}}`
