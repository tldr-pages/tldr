# bun pm տարբերակ

> Կառավարեք `version` դաշտը `package.json`-ում:.
> Լրացուցիչ տեղեկություններ. <https://bun.com/docs/pm/cli/pm#version>:.

- Ցուցադրել ընթացիկ փաթեթի տարբերակը.:

`bun pm version`

- Սահմանեք հատուկ տարբերակ.:

`bun pm version {{9.0.1}}`

- Բացեք տարբերակը՝ օգտագործելով իմաստային տարբերակի տեսակը (`major`, `minor`, `patch` և այլն):

`bun pm version {{major|minor|patch|premajor|preminor|prepatch|prerelease}}`

- Սահմանեք տարբերակը հիմնված Git թեգերի վրա.:

`bun pm version from-git`
