# az պահեստավորման հերթ

> Կառավարեք պահեստավորման հերթերը Azure-ում:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/storage/queue>:.

- Ստեղծեք հերթ.:

`az storage queue create --account-name {{storage_account_name}} {{[-n|--name]}} {{queue_name}} --metadata {{queue_metadata}}`

- Ստեղծեք համօգտագործվող մուտքի ստորագրություն հերթի համար.:

`az storage queue generate-sas --account-name {{storage_account_name}} {{[-n|--name]}} {{queue_name}} --permissions {{queue_permissions}} --expiry {{expiry_date}} --https-only`

- Թվարկեք հերթերը պահեստային հաշվում.:

`az storage queue list --prefix {{filter_prefix}} --account-name {{storage_account_name}}`

- Ջնջել նշված հերթը և ցանկացած հաղորդագրություն, որը պարունակում է.:

`az storage queue delete --account-name {{storage_account_name}} {{[-n|--name]}} {{queue_name}} --fail-not-exist`
