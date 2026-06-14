# az պահեստավորման սեղան

> Կառավարեք NoSQL բանալի-արժեքի պահեստավորումը Azure-ում:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/storage/table>:.

- Ստեղծեք նոր աղյուսակ պահեստային հաշվում.:

`az storage table create --account-name {{storage_account_name}} {{[-n|--name]}} {{table_name}} --fail-on-exist`

- Ստեղծեք ընդհանուր մուտքի ստորագրություն աղյուսակի համար.:

`az storage table generate-sas --account-name {{storage_account_name}} {{[-n|--name]}} {{table_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --https-only`

- Թվարկեք աղյուսակները պահեստային հաշվի մեջ.:

`az storage table list --account-name {{storage_account_name}}`

- Ջնջել նշված աղյուսակը և ցանկացած տվյալ, որը պարունակում է.:

`az storage table delete --account-name {{storage_account_name}} {{[-n|--name]}} {{table_name}} --fail-not-exist`
