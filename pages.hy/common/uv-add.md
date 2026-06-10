# uv ավելացնել

> Ավելացրեք փաթեթի կախվածությունը `pyproject.toml` ֆայլին:.
> Փաթեթները նշված են ըստ <https://peps.python.org/pep-0508/>:.
> Լրացուցիչ տեղեկություններ. <https://docs.astral.sh/uv/reference/cli/#uv-add>:.

- Ավելացնել փաթեթի վերջին տարբերակը.:

`uv add {{package}}`

- Ավելացնել բազմաթիվ փաթեթներ.:

`uv add {{package1 package2 ...}}`

- Ավելացնել փաթեթ՝ տարբերակի պահանջով.:

`uv add {{package>=1.2.3}}`

- Փաթեթներ ավելացրեք կամընտիր կախվածության խմբին, որը կներառվի, երբ հրապարակվի.:

`uv add --optional {{optional}} {{package1 package2 ...}}`

- Ավելացնել փաթեթներ տեղական խմբին, որը չի ներառվի, երբ հրապարակվի.:

`uv add --group {{group}} {{package1 package2 ...}}`

- Ավելացրեք փաթեթներ մշակողների խմբին, սղագրություն `--group dev`-ի համար.:

`uv add --dev {{package1 package2 ...}}`

- Ավելացնել փաթեթը որպես խմբագրելի.:

`uv add --editable {{path/to/package}}/`

- Միացրեք լրացուցիչ փաթեթը տեղադրելիս, որը կարող է տրամադրվել մի քանի անգամ.:

`uv add {{package}} --extra {{extra_feature}}`
