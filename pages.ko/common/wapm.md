# wapm

> WebAssembly 패키지 관리자.
> 더 많은 정보: <https://wapm.io/help/reference>.

- 상호 작용 방식으로 새로운 `wapm.toml` 파일 생성:

`wapm init`

- `wapm.toml`에 나열된 모든 패키지 의존성 다운로드:

`wapm install`

- 특정 버전의 패키지를 다운로드하고 `wapm.toml`의 의존성 목록에 추가:

`wapm install {{패키지}}@{{버전}}`

- 패키지를 다운로드하여 전역으로 설치:

`wapm install --global {{패키지}}`

- 패키지를 제거하고 `wapm.toml`의 의존성 목록에서 삭제:

`wapm uninstall {{패키지}}`

- 로컬에 설치된 의존성 트리 출력:

`wapm list`

- 최상위 전역 설치 패키지 나열:

`wapm list --global`

- Wasmer 런타임을 사용하여 패키지 명령 실행:

`wapm run {{명령_이름}} {{인수}}`
