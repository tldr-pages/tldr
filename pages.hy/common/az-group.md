#ազ խումբ

> Կառավարեք ռեսուրսների խմբերը և ձևանմուշների տեղակայումը:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/group>:.

- Ստեղծեք նոր ռեսուրսների խումբ.:

`az group create {{[-n|--name]}} {{name}} {{[-l|--location]}} {{location}}`

- Ստուգեք, արդյոք ռեսուրսների խումբ գոյություն ունի.:

`az group exists {{[-n|--name]}} {{name}}`

- Ջնջել ռեսուրսների խումբը.:

`az group delete {{[-n|--name]}} {{name}}`

- Սպասեք, մինչև ռեսուրսների խմբի պայմանը կատարվի.:

`az group wait {{[-n|--name]}} {{name}} --{{created|deleted|exists|updated}}`
