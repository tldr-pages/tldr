# reflex

> 특정 파일이 변경되면 디렉토리를 모니터링하고 명령을 다시 실행.
> 더 많은 정보: <https://github.com/cespare/reflex>.

- 파일이 변경되면 `make`로 다시 빌드:

`reflex make`

- `.go` 파일이 변경되면 Go 애플리케이션을 컴파일하고 실행:

`reflex --regex='{{\.go$}}' {{go run .}}`

- 변경 사항을 모니터링할 때 디렉토리를 무시:

`reflex --inverse-regex='{{^dir/}}' {{명령어}}`

- `reflex`가 시작될 때 명령어를 실행하고 파일이 변경되면 다시 시작:

`reflex --start-service=true {{명령어}}`

- 변경된 파일 이름을 대체하여 출력:

`reflex -- echo {}`
