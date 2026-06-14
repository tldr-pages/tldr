# gh gpg-բանալին

> Կառավարեք GPG ստեղները, որոնք գրանցված են լիազորված GitHub հաշվում:.
> Տես նաև՝ `gpg`:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_gpg-key>:.

- Նշեք GPG ստեղները լիազորված GitHub հաշվում.:

`gh gpg-key {{[ls|list]}}`

- Ավելացրեք GPG բանալի լիազորված GitHub հաշվին՝ նշելով հիմնական ֆայլը.:

`gh gpg-key add {{path/to/key_file}}`

- Ավելացրեք GPG բանալի լիազորված GitHub հաշվին՝ նշելով բանալու ID-ն.:

`gpg {{[-a|--armor]}} --export {{key_id}} | gh gpg-key add -`

- Ջնջել GPG ստեղնը լիազորված GitHub հաշվից.:

`gh gpg-key delete {{key_id}}`
