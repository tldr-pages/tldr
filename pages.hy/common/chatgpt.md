# chatgpt

> Shell սկրիպտը՝ OpenAI-ի ChatGPT և DALL-E տերմինալից օգտագործելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/0xacx/chatGPT-shell-cli>:.

- Սկսեք զրույցի ռեժիմում.:

`chatgpt`

- Հուշում տվեք պատասխանել.:

`chatgpt {{[-p|--prompt]}} "{{What is the regex to match an email address?}}"`

- Սկսեք զրույցի ռեժիմում՝ օգտագործելով որոշակի մոդել (կանխադրվածը `gpt-3.5-turbo` է):

`chatgpt {{[-m|--model]}} {{gpt-4}}`

- Սկսեք զրույցի ռեժիմում նախնական հուշումով.:

`chatgpt {{[-i|--init-prompt]}} "{{You are Rick, from Rick and Morty. Respond to questions using his mannerism and include insulting jokes.}}"`

- Հրամանի արդյունքը ուղարկեք `chatgpt` որպես հուշում.:

`echo "{{How to view running processes on Ubuntu?}}" | chatgpt`

- Ստեղծեք պատկեր DALL-E-ի միջոցով.:

`chatgpt {{[-p|--prompt]}} "{{image: A white cat}}"`
