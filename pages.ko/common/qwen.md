# qwen

> Qwen3-Coder와 대화형 프롬프트를 실행.
> 관련 항목: `gemini`.
> 더 많은 정보: <https://github.com/QwenLM/qwen-code>.

- 대화형 REPL 세션 시작:

`qwen`

- 다른 명령의 출력을 Qwen에 전달하여 처리한 후 종료:

`{{echo "Summarize the history of Rome"}} | qwen {{[-p|--prompt]}}`

- 기본 모델 재정의 (기본값: qwen3-coder-max):

`qwen {{[-m|--model]}} {{모델_이름}}`

- 샌드박스 컨테이너에서 실행:

`qwen {{[-s|--sandbox]}}`

- 프롬프트를 실행한 후 대화형 모드 유지:

`qwen {{[-i|--prompt-interactive]}} "{{Give me an example of recursion in Python}}"`

- 모든 파일을 컨텍스트에 포함:

`qwen {{[-a|--all-files]}}`

- 상태 표시줄에 메모리 사용량 표시:

`qwen --show-memory-usage`
