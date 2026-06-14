# բանաստեղծական տարբերակ

> Կառավարեք Poetry նախագծի տարբերակը:.
> Ենթադրում է ծրագրի հետևյալ փուլերը՝ `patch`, `minor`, `major`, `prepatch`, `preminor`, `premajor`, `prerelease`:.
> Տես նաև՝ `asdf`:.
> Լրացուցիչ տեղեկություններ. <https://python-poetry.org/docs/cli/#version>:.

- Արտադրեք ընթացիկ տարբերակը.:

`poetry version {{[-s|--short]}}`

- Նախագիծը դնել որոշակի փուլի.:

`poetry version {{stage}}`

- Ավելացրեք նախագիծը հաջորդ նախնական թողարկման փուլ.:

`poetry version --next-phase`

- Փորձարկեք նախագծի փուլի ֆունկցիան՝ առանց `pyproject.toml`-ին գրելու:

`poetry version {{stage}} --dry-run`
