# mise

> 다양한 패키지의 버전을 관리.
> 더 많은 정보: <https://mise.jdx.dev/cli/>.

- 사용 가능한 모든 플러그인 나열:

`mise plugins list-all`

- 플러그인 설치:

`mise plugins add {{이름}}`

- 설치 가능한 런타임 버전 나열:

`mise ls-remote {{이름}}`

- 특정 버전의 패키지 설치:

`mise install {{이름}}@{{버전}}`

- 패키지의 전역 버전 설정:

`mise use --global {{이름}}@{{버전}}`

- 패키지의 로컬 버전 설정:

`mise use {{이름}}@{{버전}}`

- 구성에서 환경 변수 설정:

`mise set {{변수}}={{값}}`
