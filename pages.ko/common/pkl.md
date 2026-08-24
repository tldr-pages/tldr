# pkl

> Pkl 설정 모듈 관리, 평가, 테스트.
> 더 많은 정보: <https://pkl-lang.org/main/current/pkl-cli/>.

- 지정한 Pkl 모듈을 평가하고 렌더링 결과를 생성:

`pkl eval {{모듈.pkl}}`

- `stdin` 및 `stdout`을 통해 통신하는 서버로 실행:

`pkl server`

- Pkl 모듈을 테스트로 실행하고 보고서 생성:

`pkl test {{모듈.pkl}}`

- REPL 세션 시작:

`pkl repl`

- Pkl 프로젝트를 패키지로 배포할 수 있도록 준비:

`pkl project package {{경로/대상/프로젝트_디렉토리}}`

- 프로젝트 의존성을 해결하고 `PklProject.deps.json` 파일에 기록:

`pkl project resolve {{경로/대상/프로젝트_디렉토리}}`
