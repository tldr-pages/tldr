# az պահեստ

> Կառավարեք Azure Cloud Storage ռեսուրսները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/storage>:.

- Ստեղծեք պահեստային հաշիվ՝ նշելով գտնվելու վայրը.:

`az storage account create {{[-g|--resource-group]}} {{group_name}} {{[-n|--name]}} {{account_name}} {{[-l|--location]}} {{location}} --sku {{account_sku}}`

- Նշեք բոլոր պահեստային հաշիվները ռեսուրսների խմբի մեջ.:

`az storage account list {{[-g|--resource-group]}} {{group_name}}`

- Թվարկեք պահեստային հաշվի մուտքի բանալիները.:

`az storage account keys list {{[-g|--resource-group]}} {{group_name}} {{[-n|--name]}} {{account_name}}`

- Ջնջել պահեստային հաշիվը.:

`az storage account delete {{[-g|--resource-group]}} {{group_name}} {{[-n|--name]}} {{account_name}}`

- Թարմացրեք նվազագույն tls տարբերակի կարգավորումը պահեստային հաշվի համար.:

`az storage account update --min-tls-version {{TLS1_0|TLS1_1|TLS1_2}} {{[-g|--resource-group]}} {{group_name}} {{[-n|--name]}} {{account_name}}`
