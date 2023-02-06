# az term

> Kezelje a piactéri megállapodást a marketplaceordering segítségével. A `azure-cli` weboldal része. További információ: <https://learn.microsoft.com/cli/azure/term>.

- Piactéri feltételek nyomtatása:

`az term show --product "{{product_identifier}}" --plan "{{plan_identifier}}" --publisher "{{publisher_identifier}}"`

- Piactéri feltételek elfogadása:

`az term accept --product "{{product_identifier}}" --plan "{{plan_identifier}}" --publisher "{{publisher_identifier}}"`
