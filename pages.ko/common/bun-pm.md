# bun pm

> Bun 패키지 매니저와 관련된 유틸리티 모음.
> `pack`, `pkg`와 같은 일부 하위 명령어는 별도의 사용법 문서를 가짐.
> 더 많은 정보: <https://bun.com/docs/pm/cli/pm>.

- 현재 워크스페이스를 tarball로 생성:

`bun pm pack`

- `bin` 디렉토리 경로 출력:

`bun pm bin`

- 기본적으로 신뢰된 의존성 목록 출력:

`bun pm default-trusted`

- npm 레지스트리 사용자 이름 출력:

`bun pm whoami`

- 현재 lockfile의 해시 생성 및 출력:

`bun pm hash`

- 스크립트를 포함한 현재 비신뢰 의존성 목록 출력:

`bun pm untrusted`

- 다른 패키지 매니저의 lockfile을 설치 없이 마이그레이션 :

`bun pm migrate`

- `package.json`에서 특정 속성 값 가져오기:

`bun pm pkg get {{프로퍼티}}`
