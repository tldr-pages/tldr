# llm

> 원격 API 및 로컬에서 설치 및 실행할 수 있는 모델을 통해 대형 언어 모델(LLM)과 상호 작용.
> 더 많은 정보: <https://llm.datasette.io/en/stable/help.html>.

- OpenAI API 키 설정:

`llm keys set openai`

- 프롬프트 실행:

`llm "{{펠리칸 애완동물에게 어울리는 재미있는 이름 10개}}"`

- 파일에 대해 [s]시스템 프롬프트 실행:

`cat {{경로/대상/파일.py}} | llm --system "{{이 코드를 설명하세요}}"`

- LLM과 동일한 환경에 PyPI에서 패키지 설치:

`llm install {{패키지1 패키지2 ...}}`

- [m]모델을 다운로드하고 프롬프트 실행:

`llm --model {{orca-mini-3b-gguf2-q4_0}} "{{프랑스의 수도는 어디인가요?}}"`

- [s]시스템 프롬프트를 생성하고 템플릿 이름으로 [s]저장:

`llm --system '{{당신은 지각 있는 치즈케이크입니다}}' --save {{지각있는_치즈케이크}}`

- 특정 [m]모델과 특정 [t]템플릿을 사용하여 대화형 채팅:

`llm chat --model {{chatgpt}} --template {{지각있는_치즈케이크}}`
