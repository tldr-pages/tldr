# պոեզիայի ստուգում

> Կառավարեք Poetry ֆայլի վավերացումը և հետևողականությունը:.
> Տես նաև՝ `asdf`:.
> Լրացուցիչ տեղեկություններ. <https://python-poetry.org/docs/cli/#check>:.

- Ստուգեք վավերացումը և համապատասխանությունը `pyproject.toml`-ի և `poetry.lock`-ի միջև պոեզիայի համար.:

`poetry check`

- Ստուգեք, որ `poetry.lock` գոյություն ունի՝:

`poetry check --lock`

- Չհաջողվեց, եթե զգուշացումներ հաղորդվեն.:

`poetry check --strict`
