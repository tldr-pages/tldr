# qwen

> Գործարկեք ինտերակտիվ հուշում Qwen3-Coder-ի հետ:.
> Տես նաև՝ `gemini`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/QwenLM/qwen-code>:.

- Սկսեք REPL նիստ՝ ինտերակտիվ զրուցելու համար.:

`qwen`

- Ուղարկեք մեկ այլ հրամանի արդյունքը Qwen և անմիջապես դուրս եկեք.:

`{{echo "Summarize the history of Rome"}} | qwen {{[-p|--prompt]}}`

- Անտեսել լռելյայն մոդելը (կանխադրված՝ qwen3-coder-max):

`qwen {{[-m|--model]}} {{model_name}}`

- Վազիր ավազատուփի կոնտեյների մեջ.:

`qwen {{[-s|--sandbox]}}`

- Կատարեք հուշում, ապա մնացեք ինտերակտիվ ռեժիմում.:

`qwen {{[-i|--prompt-interactive]}} "{{Give me an example of recursion in Python}}"`

- Ներառեք բոլոր ֆայլերը համատեքստում.:

`qwen {{[-a|--all-files]}}`

- Ցույց տալ հիշողության օգտագործումը կարգավիճակի տողում.:

`qwen --show-memory-usage`
