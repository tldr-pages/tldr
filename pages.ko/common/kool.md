# kool

> 소프트웨어 개발 환경을 구축.
> 더 많은 정보: <https://kool.dev/docs/commands-reference/kool>.

- 특정 프리셋을 사용하여 프로젝트 생성:

`kool create {{프리셋}} {{프로젝트_이름}}`

- 현재 디렉토리의 `kool.yml` 파일에 정의된 특정 스크립트 실행:

`kool run {{스크립트}}`

- 현재 디렉토리의 서비스 시작/중지:

`kool {{start|stop}}`

- 현재 디렉토리의 서비스 상태 표시:

`kool status`

- 최신 버전으로 업데이트:

`kool self-update`

- 지정된 셸에 대한 자동 완성 스크립트 출력:

`kool completion {{bash|fish|powershell|zsh}}`
