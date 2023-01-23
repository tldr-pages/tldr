# terraform plan

> Terraform végrehajtási tervek generálása és megjelenítése. További információ: <https://www.terraform.io/docs/cli/commands/plan.html>.

- A végrehajtási terv generálása és megjelenítése az aktuális könyvtárban:

`terraform plan`

- Az összes jelenleg létező távoli objektum megsemmisítésére vonatkozó terv megjelenítése:

`terraform plan -destroy`

- A Terraform állapot és a kimeneti értékek frissítésére vonatkozó terv megjelenítése:

`terraform plan -refresh-only`

- A bemeneti változók értékeinek megadása:

`terraform plan -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- A Terraform figyelmének csak az erőforrások egy részhalmazára összpontosítása:

`terraform plan -target {{resource_type.resource_name[instance index]}}`

- A terv JSON-ként történő kiadása:

`terraform plan -json`

- Terv írása egy adott fájlba:

`terraform plan -no-color > {{path/to/file}}`
