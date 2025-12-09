# openai

> OpenAI API에 접근할 수 있는 CLI 도구.
> 더 많은 정보: <https://github.com/openai/openai-python>.

- 모델 나열:

`openai api models.list`

- 완료 생성:

`openai api completions.create --model {{ada}} --prompt "{{Hello world}}"`

- 채팅 완료 생성:

`openai api chat_completions.create --model {{gpt-3.5-turbo}} --message {{user "Hello world"}}`

- DALL·E API를 통해 이미지 생성:

`openai api image.create --prompt "{{two dogs playing chess, cartoon}}" --num-images {{1}}`
