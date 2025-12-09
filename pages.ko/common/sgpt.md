# sgpt

> OpenAI의 GPT 모델로 구동되는 명령줄 생산성 도구.
> 더 많은 정보: <https://github.com/TheR1D/shell_gpt#readme>.

- 검색 엔진으로 사용하여 태양의 질량을 묻기:

`sgpt "{{태양의 질량}}"`

- 쉘 명령 실행, 현재 디렉토리의 모든 파일에 `chmod 444` 적용:

`sgpt --shell "{{현재 디렉토리의 모든 파일을 읽기 전용으로 설정}}"`

- 코드 생성, 클래식한 fizz buzz 문제 해결:

`sgpt --code "{{Python을 사용하여 fizz buzz 문제 해결}}"`

- 고유한 세션 이름으로 채팅 세션 시작:

`sgpt --chat {{세션_이름}} "{{내가 좋아하는 숫자를 기억해 주세요: 4}}"`

- `REPL` (Read-eval-print loop) 세션 시작:

`sgpt --repl {{명령}}`

- 도움말 표시:

`sgpt --help`
