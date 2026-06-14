# az պահեստային հաշիվ

> Կառավարեք պահեստային հաշիվները Azure-ում:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/storage/account>:.

- Ստեղծեք պահեստային հաշիվ.:

`az storage account create {{[-n|--name]}} {{storage_account_name}} {{[-g|--resource-group]}} {{azure_resource_group}} --location {{azure_location}} --sku {{storage_account_sku}}`

- Ստեղծեք ընդհանուր մուտքի ստորագրություն հատուկ պահեստային հաշվի համար.:

`az storage account generate-sas --account-name {{storage_account_name}} {{[-n|--name]}} {{account_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --services {{storage_services}} --resource-types {{resource_types}}`

- Ցուցակեք պահեստային հաշիվները.:

`az storage account list {{[-g|--resource-group]}} {{azure_resource_group}}`

- Ջնջել հատուկ պահեստային հաշիվ.:

`az storage account delete {{[-n|--name]}} {{storage_account_name}} {{[-g|--resource-group]}} {{azure_resource_group}}`
