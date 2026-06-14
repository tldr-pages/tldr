#լմ

> Շփվեք մեծ լեզուների մոդելների (LLM) հետ հեռավոր API-ների և մոդելների միջոցով, որոնք կարող են տեղադրվել և գործարկվել ձեր մեքենայում:.
> Լրացուցիչ տեղեկություններ. <https://llm.datasette.io/en/stable/help.html>:.

- Ստեղծեք OpenAI API բանալի.:

`llm keys set openai`

- Գործարկեք հուշում.:

`llm "{{Ten fun names for a pet pelican}}"`

- Գործարկեք համակարգի հուշումը ֆայլի դեմ.:

`cat {{path/to/file.py}} | llm {{[-s|--system]}} "{{Explain this code}}"`

- Տեղադրեք փաթեթներ PyPI-ից նույն միջավայրում, ինչ LLM.:

`llm install {{package1 package2 ...}}`

- Ներբեռնեք և գործարկեք հուշում մոդելի դեմ.:

`llm {{[-m|--model]}} {{orca-mini-3b-gguf2-q4_0}} "{{What is the capital of France?}}"`

- Ստեղծեք համակարգի հուշում և պահպանեք այն կաղապարի անունով.:

`llm {{[-s|--system]}} '{{You are a sentient cheesecake}}' --save {{sentient_cheesecake}}`

- Ինտերակտիվ զրույց վարեք կոնկրետ մոդելի հետ՝ օգտագործելով հատուկ ձևանմուշ.:

`llm chat {{[-m|--model]}} {{chatgpt}} {{[-t|--template]}} {{sentient_cheesecake}}`
