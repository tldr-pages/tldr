# az թեգ

> Կառավարեք պիտակները ռեսուրսի վրա:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/tag>:.

- Ստեղծեք պիտակի արժեք.:

`az tag add-value {{[-n|--name]}} {{tag_name}} --value {{tag_value}}`

- Բաժանորդագրության մեջ պիտակ ստեղծեք.:

`az tag create {{[-n|--name]}} {{tag_name}}`

- Ջնջել պիտակը բաժանորդագրությունից.:

`az tag delete {{[-n|--name]}} {{tag_name}}`

- Թվարկեք բոլոր պիտակները բաժանորդագրության վրա.:

`az tag list --resource-id /subscriptions/{{subscription_id}}`

- Ջնջել պիտակի արժեքը որոշակի պիտակի անվան համար.:

`az tag remove-value {{[-n|--name]}} {{tag_name}} --value {{tag_value}}`
