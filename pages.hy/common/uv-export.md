# ուլտրամանուշակագույն արտահանում

> Արտահանել նախագծի կողպեքի ֆայլը այլընտրանքային ձևաչափով:.
> Լրացուցիչ տեղեկություններ. <https://docs.astral.sh/uv/reference/cli/#uv-export>:.

- Արտահանել կախվածությունները `requirements.txt` ֆայլ՝:

`uv export --format requirements-txt {{[-o|--output-file]}} {{requirements.txt}}`

- Արտահանել կախվածությունները `pylock.toml` ձևաչափով՝:

`uv export --format pylock.toml`

- Արտահանել միայն արտադրական կախվածությունները (բացառել մշակողի կախվածությունը).:

`uv export --no-dev`

- Արտահանել, ներառյալ հատուկ կամընտիր կախվածության խումբ.:

`uv export --extra {{group_name}}`

- Արտահանել, ներառյալ բոլոր կամընտիր կախվածությունները.:

`uv export --all-extras`

- Արտահանում, ներառյալ հատուկ կախվածության խումբ.:

`uv export --group {{group_name}}`

- Արտահանել առանց հեշերի.:

`uv export --no-hashes`

- Արտահանել կախվածությունը կոնկրետ փաթեթի համար աշխատանքային տարածքում.:

`uv export --package {{package_name}}`
