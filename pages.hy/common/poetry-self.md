# պոեզիա-ես

> Կառավարեք Poetry-ի տեղադրման/գործարկման միջավայրն ինքնին:.
> Այս հրամանները վերաբերում են `pyproject.toml` և `poetry.lock` ֆայլերին ձեր Poetry կազմաձևման գրացուցակում:.
> Տես նաև՝ `asdf`:.
> Լրացուցիչ տեղեկություններ. <https://python-poetry.org/docs/cli/#self>:.

- Տեղադրեք փաթեթ.:

`poetry self add {{package_name}}`

- Տեղադրեք կախվածությունները Poetry-ի տեղադրման `pyproject.toml` ֆայլից.:

`poetry self install`

- Կողպեք կախվածությունը Poetry-ի տեղադրման `pyproject.toml` ֆայլից.:

`poetry self lock`

- Հեռացնել փաթեթը.:

`poetry self remove {{package_name}}`

- Նշեք բոլոր տեղադրված փաթեթները.:

`poetry self show`

- Թվարկեք բոլոր տեղադրված պլագինները.:

`poetry self show plugins`

- Համաժամացրեք գործարկման միջավայրը Poetry-ի տեղադրման `poetry.lock` ֆայլի հետ.:

`poetry self sync`

- Թարմացրեք կախվածությունները Poetry-ի տեղադրման `pyproject.toml` ֆայլից.:

`poetry self update`
