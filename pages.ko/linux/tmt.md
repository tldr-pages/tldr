# tmt

> 테스트를 생성, 실행, 디버깅하기 위한 테스트 관리 도구.
> `run`, `try`와 같은 하위 명령어는 사용법 문서를 자체적으로 가짐.
> 더 많은 정보: <https://tmt.readthedocs.io/en/stable/examples.html>.

- 사용 가능한 테스트, 플랜, 스토리 목록 출력:

`tmt`

- tmt 파일/프로젝트 구조 초기화:

`tmt init`

- 템플릿과 링크를 사용해 새로운 테스트 생성:

`tmt test create {{[-t|--template]}} {{beakerlib}} --link {{verifies:issue#1234}}`

- 테스트, 플랜, 스토리 목록 출력:

`tmt {{test|plan|story}} ls {{패턴}}`

- 특정 컨텍스트에서 테스트 메타데이터 상세 출력:

`tmt {{[-c|--context]}} {{arch=aarch64}} test show`

- tmt 파일을 스펙에 맞게 검증:

`tmt lint`

- filter 사용:

`tmt tests ls {{[-f|--filter]}} {{tag:foo}} {{[-f|--filter]}} {{tier:0}}`

- 도움말 표시:

`tmt --help`
