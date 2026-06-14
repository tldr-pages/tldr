# asdf

> Կառավարեք տարբեր փաթեթների տարբերակները:.
> Լրացուցիչ տեղեկություններ. <https://asdf-vm.com/manage/commands.html>:.

- Թվարկեք բոլոր հասանելի հավելվածները.:

`asdf plugin list all`

- Տեղադրեք plugin.:

`asdf plugin add {{name}}`

- Թվարկեք փաթեթի բոլոր հասանելի տարբերակները.:

`asdf list all {{name}}`

- Տեղադրեք փաթեթի որոշակի տարբերակ.:

`asdf install {{name}} {{version}}`

- Սահմանեք գլոբալ տարբերակը փաթեթի համար.:

`asdf set -u {{name}} {{version}}`

- Սահմանեք տեղական տարբերակը փաթեթի համար.:

`asdf set {{name}} {{version}}`

- Տես փաթեթի համար օգտագործվող ընթացիկ տարբերակը.:

`asdf current {{name}}`
