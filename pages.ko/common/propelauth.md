# propelauth

> PropelAuth 인증을 빠르고 간편하게 설정하는 CLI 도구.
> 더 많은 정보: <https://docs.propelauth.com/reference/api/cli>.

- <https://auth.propelauth.com/api_keys/personal> 로부터 생성된 API 키를 사용하여 PropelAuth에 로그인:

`propelauth login`

- CLI에서 사용할 기본 PropelAuth 프로젝트 설정. (기본 프로젝트가 설정되어 있지 않으면, 특정 명령을 실행할 때마다 프로젝트를 선택하라는 메시지가 표시됨):

`propelauth set-default-project`

- 애플리케이션에 PropelAuth 인증 설치. (디렉터리를 지정하지 않으면 현재 디렉터리 사용):

`propelauth setup {{[-f|--framework]}} {{경로/대상/디렉터리}}`

- PropelAuth에서 CLI로 로그아웃:

`propelauth logout`
