# pokeget

> Ցուցադրեք Pokemon-ի ոգին ձեր տերմինալում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/talwat/pokeget-rs>:.

- Տպեք տրված պոկեմոնի սփրայթը.:

`pokeget {{pokemon_name}}`

- Տպել Mr. Mime (նկատի ունեցեք `-`-ի օգտագործումը բացատների փոխարեն):

`pokeget mr-mime`

- Տպել Mega Gengar:

`pokeget gengar {{[-m|--mega]}}`

- Տպեք պատահական փայլուն պոկեմոն.:

`pokeget random {{[-s|--shiny]}}`

- Տպեք Alolan Meowth-ը, առանց Pokemon-ի անունը տպելու.:

`pokeget meowth {{[-a|--alolan]}} --hide-name`

- Տպեք պատահական պոկեմոն՝ փայլուն լինելու 1/4096 հնարավորությամբ.:

`((RANDOM%4096 == 0)) && pokeget random --shiny || pokeget random`
