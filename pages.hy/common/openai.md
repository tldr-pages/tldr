#բաց

> CLI գործիք, որն ապահովում է OpenAI API-ին հասանելիություն:.
> Լրացուցիչ տեղեկություններ. <https://github.com/openai/openai-python>:.

- Ցուցակ մոդելներ.:

`openai api models.list`

- Ստեղծեք ավարտ.:

`openai api completions.create --model {{ada}} --prompt "{{Hello world}}"`

- Ստեղծեք զրույցի ավարտ.:

`openai api chat_completions.create --model {{gpt-3.5-turbo}} --message {{user "Hello world"}}`

- Ստեղծեք պատկերներ DALL·E API-ի միջոցով.:

`openai api image.create --prompt "{{two dogs playing chess, cartoon}}" --num-images {{1}}`
