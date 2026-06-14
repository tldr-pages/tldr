# az պահեստավորման բլբ

> Կառավարեք բլբի պահեստավորման տարաները և առարկաները Azure-ում:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/storage/blob>:.

- Ներբեռնեք բշտիկ ֆայլի ուղու վրա, որը նշում է աղբյուրի կոնտեյները.:

`az storage blob download --account-name {{account_name}} --account-key {{account_key}} {{[-c|--container-name]}} {{container_name}} {{[-n|--name]}} {{blob_name}} {{[-f|--file]}} {{path/to/file}}`

- Ներբեռնեք բշտիկները բլբի կոնտեյներից ռեկուրսիվ կերպով.:

`az storage blob download-batch --account-name {{account_name}} --account-key {{account_key}} {{[-s|--source]}} {{container_name}} --pattern {{filename_regex}} {{[-d|--destination]}} {{path/to/destination}}`

- Վերբեռնեք տեղական ֆայլ blob պահեստում.:

`az storage blob upload --account-name {{account_name}} --account-key {{account_key}} {{[-c|--container-name]}} {{container_name}} {{[-n|--name]}} {{blob_name}} {{[-f|--file]}} {{path/to/file}}`

- Ջնջել բլբի օբյեկտը.:

`az storage blob delete --account-name {{account_name}} --account-key {{account_key}} {{[-c|--container-name]}} {{container_name}} {{[-n|--name]}} {{blob_name}}`

- Ստեղծեք ընդհանուր մուտքի ստորագրություն բլբի համար.:

`az storage blob generate-sas --account-name {{account_name}} --account-key {{account_key}} {{[-c|--container-name]}} {{container_name}} {{[-n|--name]}} {{blob_name}} --permissions {{permission_set}} --expiry {{Y-m-d'T'H:M'Z'}} --https-only`
