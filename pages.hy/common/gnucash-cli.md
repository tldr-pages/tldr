# gnucash-cli

> GnuCash-ի հրամանի տող տարբերակ:.
> Լրացուցիչ տեղեկություններ. <https://gnucash.org/viewdoc.phtml?rev=5&lang=C&doc=help>:.

- Ստացեք գնանշումներ արժույթների և բաժնետոմսերի համար, որոնք նշված են ֆայլում և տպեք դրանք.:

`gnucash-cli {{[-Q|--quotes]}} get {{path/to/file.gnucash}}`

- Ստեղծեք որոշակի տեսակի ֆինանսական հաշվետվություն՝ նշված `--name`-ով.:

`gnucash-cli --report run --name "{{Balance Sheet}}" {{path/to/file.gnucash}}`
