# vllm chat

> 실행 중인 API 서버를 통해 OpenAI 호환 REST API를 사용하여 대화 완성을 생성합니다.
> 더 많은 정보: <https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html>.

- API 서버에 단일 채팅 프롬프트를 보내고 응답 받기:

`vllm chat --quick "{{메시지}}"`

- 특정 모델 이름을 지정하여 대화하기:

`vllm chat --model-name {{모델_이름}} --quick "{{메시지}}"`

- 사용자 정의 시스템 프롬프트로 대화하기:

`vllm chat --system-prompt "{{시스템_프롬프트}}" --quick "{{메시지}}"`

- 사용자 정의 API 서버 URL을 사용하여 대화하기:

`vllm chat --url {{http://사용자지정-호스트:포트/v1}} --quick "{{메시지}}"`

- 인증용 API 키를 지정하여 대화하기:

`vllm chat --api-key {{사용자_api_키}} --quick "{{메시지}}"`

- 대화형 채팅 세션 시작:

`vllm chat`
