# az config

> Կառավարեք Azure CLI կոնֆիգուրացիան:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/config>:.

- Տպել բոլոր կոնֆիգուրացիաները.:

`az config get`

- Տպել կոնֆիգուրացիաներ որոշակի բաժնի համար.:

`az config get {{section_name}}`

- Սահմանեք կոնֆիգուրացիա.:

`az config set {{configuration_name}}={{value}}`

- Չեղարկել կոնֆիգուրացիան.:

`az config unset {{configuration_name}}`
