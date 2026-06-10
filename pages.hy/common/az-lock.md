# az կողպեք

> Կառավարեք Azure կողպեքները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/lock>:.

- Ստեղծեք միայն կարդալու համար բաժանորդագրության մակարդակի կողպեք.:

`az lock create {{[-n|--name]}} {{lock_name}} {{[-t|--lock-type]}} ReadOnly`

- Ստեղծեք միայն կարդալու ռեսուրսների խմբի մակարդակի կողպեք.:

`az lock create {{[-n|--name]}} {{lock_name}} {{[-g|--resource-group]}} {{group_name}} {{[-t|--lock-type]}} ReadOnly`

- Ջնջել բաժանորդագրության մակարդակի կողպեքը.:

`az lock delete {{[-n|--name]}} {{lock_name}}`

- Ջնջել ռեսուրսների խմբի մակարդակի կողպեքը.:

`az lock delete {{[-n|--name]}} {{lock_name}} {{[-g|--resource-group]}} {{group_name}}`

- Թվարկեք բոլոր կողպեքները բաժանորդագրության մակարդակում.:

`az lock list`

- Ցույց տալ բաժանորդագրության մակարդակի կողպեքը հատուկ անունով.:

`az lock show {{[-n|--name]}} {{lock_name}}`
