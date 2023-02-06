# az storage

> Azure Cloud Storage erőforrások kezelése. A `azure-cli` weboldal része. További információ: <https://learn.microsoft.com/cli/azure/storage>.

- Hozzon létre egy tárolófiókot:

`az storage account create -g {{group_name}} -n {{account_name}} -l {{location}} --sku {{account_sku}}`

- Az erőforráscsoportban lévő összes tárolófiók listázása:

`az storage account list -g {{group_name}}`

- Egy tárolófiók hozzáférési kulcsainak listázása:

`az storage account keys list -g {{group_name}} -n {{account_name}}`

- Tárolófiók törlése:

`az storage account delete -g {{group_name}} -n {{account_name}}`

- A minimális tls verzió beállítás frissítése egy tárolófiókhoz:

`az storage account update --min-tls-version TLS1_2 -g {{group_name}} -n {{account_name}}`
