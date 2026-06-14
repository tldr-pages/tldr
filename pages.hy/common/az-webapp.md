# az webapp

> Կառավարեք Azure Cloud Services-ում տեղակայված վեբ հավելվածները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/webapp>:.

- Ցուցակեք վեբ հավելվածի համար հասանելի գործարկման ժամանակները.:

`az webapp list-runtimes {{[-os|--os-type]}} {{windows|linux}}`

- Ստեղծեք վեբ հավելված.:

`az webapp up {{[-n|--name]}} {{name}} {{[-l|--location]}} {{location}} {{[-r|--runtime]}} {{runtime}}`

- Թվարկեք բոլոր վեբ հավելվածները.:

`az webapp list`

- Ջնջել հատուկ վեբ հավելված.:

`az webapp delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`
