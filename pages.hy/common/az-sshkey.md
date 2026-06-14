# ազ սշքեյ

> Կառավարեք SSH հանրային բանալիները վիրտուալ մեքենաներով:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/sshkey>:.

- Ստեղծեք նոր SSH բանալի.:

`az sshkey create --name {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Վերբեռնեք գոյություն ունեցող SSH բանալի.:

`az sshkey create --name {{name}} {{[-g|--resource-group]}} {{resource_group}} --public-key "{{@path/to/key.pub}}"`

- Նշեք բոլոր SSH հանրային բանալիները.:

`az sshkey list`

- Ցույց տալ տեղեկատվություն SSH հանրային բանալու մասին.:

`az sshkey show --name {{name}} {{[-g|--resource-group]}} {{resource_group}}`
