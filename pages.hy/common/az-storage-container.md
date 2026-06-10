# az պահեստային տարա

> Կառավարեք բլբի պահեստավորման տարաները Azure-ում:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/storage/container>:.

- Ստեղծեք կոնտեյներ պահեստային հաշվում.:

`az storage container create --account-name {{storage_account_name}} {{[-n|--name]}} {{container_name}} --public-access {{access_level}} --fail-on-exist`

- Ստեղծեք ընդհանուր մուտքի ստորագրություն կոնտեյների համար.:

`az storage container generate-sas --account-name {{storage_account_name}} {{[-n|--name]}} {{container_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --https-only`

- Նշեք բեռնարկղերը պահեստային հաշվում.:

`az storage container list --account-name {{storage_account_name}} --prefix {{filter_prefix}}`

- Նշեք նշված կոնտեյները ջնջման համար.:

`az storage container delete --account-name {{storage_account_name}} {{[-n|--name]}} {{container_name}} --fail-not-exist`
