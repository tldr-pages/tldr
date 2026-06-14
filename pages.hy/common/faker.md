#կեղծարար

> Python գրադարան և կեղծ տվյալներ ստեղծելու գործիք:.
> Լրացուցիչ տեղեկություններ. <https://faker.readthedocs.io/en/master/>:.

- Ցույց տալ բոլոր կեղծ տվյալների մատակարարներին օրինակների հետ միասին.:

`faker`

- Ստեղծեք որոշակի տեսակի կեղծ տվյալներ.:

`faker {{name|address|passport_full|credit_card_full|phone_number|email|company|date_time|user_name|password|job|...}}`

- Ստեղծեք մի շարք կեղծ հասցեներ որոշակի երկրից (օգտագործեք `localectl list-locales | cut --delimiter . --fields 1`՝ տեղանքների ցանկը ստանալու համար).:

`faker {{[-r|--repeat]}} {{number}} {{[-l|--lang]}} {{de_DE|de_CH|...}} address`

- Ստեղծեք որոշակի երկրի մի շարք քաղաքներ և դրանք թողարկեք ֆայլ (օգտագործեք `localectl list-locales | cut --delimiter . --fields 1`՝ տեղանքների ցանկը ստանալու համար).:

`faker {{[-r|--repeat]}} {{number}} {{[-l|--lang]}} {{en_AU|en_US|...}} city -o {{path/to/file.txt}}`

- Ստեղծեք մի շարք պատահական HTTP օգտատեր-գործակալներ, որոնք ցույց են տալիս մանրամասն ելք.:

`faker {{[-r|--repeat]}} {{number}} {{[-v|--verbose]}} user_agent`

- Ստեղծեք մի շարք տիրույթի անուններ և առանձնացրեք յուրաքանչյուրը հատուկ բաժանարարի միջոցով.:

`faker {{[-r|--repeat]}} {{number}} {{[-s|--sep]}} '{{,}}' domain_name`
