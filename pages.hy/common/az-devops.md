# az devops

> Կառավարեք Azure DevOps կազմակերպությունները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/devops>:.

- Սահմանեք Անձնական մուտքի նշանը (PAT)՝ որոշակի կազմակերպություն մուտք գործելու համար.:

`az devops login {{[--org|--organization]}} {{organization_url}}`

- Բացեք նախագիծ բրաուզերում.:

`az devops project show {{[-p|--project]}} {{project_name}} --open`

- Թվարկե՛ք կոնկրետ նախագծի վրա աշխատող կոնկրետ թիմի անդամներին.:

`az devops team list-member {{[-p|--project]}} {{project_name}} --team {{team_name}}`

- Ստուգեք Azure DevOps CLI-ի ընթացիկ կոնֆիգուրացիան.:

`az devops configure {{[-l|--list]}}`

- Կարգավորեք Azure DevOps CLI-ի վարքագիծը՝ սահմանելով լռելյայն նախագիծ և լռելյայն կազմակերպություն.:

`az devops configure {{[-d|--defaults]}} project={{project_name}} organization={{organization_url}}`
