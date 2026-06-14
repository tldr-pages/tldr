#երկվորյակ

> Գործարկեք ինտերակտիվ հուշում Gemini AI-ի հետ:.
> Լրացուցիչ տեղեկություններ. <https://geminicli.com/docs/cli/cli-reference/>:.

- Սկսեք REPL նիստ՝ ինտերակտիվ զրուցելու համար.:

`gemini`

- Մեկ այլ հրամանի արդյունք ուղարկեք Երկվորյակին և անմիջապես դուրս եկեք.:

`{{echo "Summarize the history of Rome"}} | gemini {{[-p|--prompt]}} -`

- Օգտագործեք հատուկ մոդել (լռելյայն՝ auto-gemini-3):

`gemini {{[-m|--model]}} {{model_name}}`

- Վազիր ավազատուփի կոնտեյների մեջ.:

`gemini {{[-s|--sandbox]}}`

- Կատարեք հուշում, ապա մնացեք ինտերակտիվ ռեժիմում.:

`gemini {{[-i|--prompt-interactive]}} "{{Give me an example of recursion in Python}}"`

- Սահմանեք հաստատման ռեժիմը գործիքի զանգերի համար.:

`gemini --approval-mode {{default|auto_edit|yolo|plan}}`

- Վերսկսեք նստաշրջանը (կանխադրված է «վերջին», ընդունում է ինդեքսի համարը կամ UUID):

`gemini {{[-r|--resume]}} {{latest|index|session_id}}`
