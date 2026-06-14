# պոեզիայի քեշ

> Կառավարեք Poetry-ի քեշը:.
> Տես նաև՝ `asdf`:.
> Լրացուցիչ տեղեկություններ. <https://python-poetry.org/docs/cli/#cache>:.

- Ցուցադրել Poetry-ի հասանելի քեշերը.:

`poetry cache list`

- Հեռացրեք բոլոր փաթեթները քեշից (օրինակ՝ PyPI).:

`poetry cache clear PyPI --all`

- Հեռացրեք որոշակի փաթեթ քեշից (Նշում. պետք է լինի `cache:package:version` ձևաչափով):

`poetry cache clear {{pypi}}:{{requests}}:{{2.24.0}}`
