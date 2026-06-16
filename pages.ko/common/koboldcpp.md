# koboldcpp

> GGML 및 GGUF 모델을 위한 AI 텍스트 생성 애플리케이션.
> 더 많은 정보: <https://github.com/LostRuins/koboldcpp/wiki#command-line-arguments-reference>.

- 하나 이상의 모델 파일 로드:

`koboldcpp {{[-m|--model]}} {{path/to/model_file}}`

- 수신 대기 포트 설정 (기본값: 5001):

`koboldcpp --port {{포트}}`

- 사용할 스레드 수 설정:

`koboldcpp {{[-t|--threads]}} {{스레드_수}}`

- 시작 완료 후 웹 브라우저 실행:

`koboldcpp --launch`

- GUI 런처 없이 시작:

`koboldcpp --skiplauncher`
