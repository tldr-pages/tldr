# chatgpt

> 터미널에서 OpenAI의 ChatGPT 및 DALL-E를 사용하기 위한 쉘 스크립트.
> 더 많은 정보: <https://github.com/0xacx/chatGPT-shell-cli>.

- 채팅 모드에서 시작:

`chatgpt`

- 다음 질문에 답하도록 프롬프트([p]rompt)를 제공:

`chatgpt {{[-p|--prompt]}} "{{이메일 주소와 일치하는 정규식은 무엇입니가?}}"`

- 특정 모델([m]odel)을 사용하여 채팅 모드에서 시작(기본값은 `gpt-3.5-turbo`입니다):

`chatgpt {{[-m|--model]}} {{gpt-4}}`

- 초기([i]nitial) 프롬프트로 채팅 모드를 시작:

`chatgpt {{[-i|--init-prompt]}} "{{당신은 Rick과 Morty의 Rick입니다. 그의 매너리즘을 사용하여 질문에 응답하고 모욕적인 농담을 포함합니다.}}"`

- 명령 결과를 `chatgpt`에 프롬프트로 파이프:

`echo "{{Ubuntu에서 실행중인 프로세스를 보는 방법?}}" | chatgpt`

- DALL-E를 사용하여 이미지를 생성:

`chatgpt {{[-p|--prompt]}} "{{image: A white cat}}"`
