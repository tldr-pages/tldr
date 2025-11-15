# tgpt

> API 키가 필요 없는 AI 챗봇과 대화.
> 사용 가능한 공급자: `openai`, `opengpts`, `koboldai`, `phind`, `llama2`, `blackboxai`.
> 더 많은 정보: <https://github.com/aandrew-me/tgpt>.

- 기본 공급자(GPT-3.5-turbo)와 대화:

`tgpt "{{프롬프트}}"`

- [m]ulti-line 대화형 모드 시작:

`tgpt --multiline`

- [i]mages 생성 후 현재 디렉토리에 저장:

`tgpt --image "{{프롬프트}}"`

- 기본 공급자(GPT-3.5-turbo)로 [c]ode 생성:

`tgpt --code "{{프롬프트}}"`

- 특정 공급자와 [q]uiet 모드(애니메이션 없이)로 대화:

`tgpt --provider {{openai|opengpts|koboldai|phind|llama2|blackboxai}} --quiet --whole "{{프롬프트}}"`

- 특정 공급자를 사용하여 [s]hell 명령 생성 및 실행(확인 프롬프트 포함):

`tgpt --provider {{llama2}} --shell "{{프롬프트}}"`

- API 키, 모델, 최대 응답 길이, 온도, `top_p`를 사용하여 프롬프트( `openai` 공급자를 사용할 때 필요):

`tgpt --provider openai --key "{{API_키}}" --model "{{gpt-3.5-turbo}}" --max-length {{10}} --temperature {{0.7}} --top_p {{0.9}} "{{프롬프트}}"`

- 추가 사전 프롬프트 입력으로 파일 삽입:

`tgpt --provider {{blackboxai}} "{{프롬프트}}" < {{경로/대상/파일}}`
