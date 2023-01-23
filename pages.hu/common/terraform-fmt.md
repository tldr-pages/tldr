# terraform fmt

> A konfiguráció formázása a Terraform nyelvi stíluskonvencióknak megfelelően. További információ: <https://www.terraform.io/docs/commands/fmt.html>.

- A konfiguráció formázása az aktuális könyvtárban:

`terraform fmt`

- A konfiguráció formázása az aktuális könyvtárban és az alkönyvtárakban:

`terraform fmt -recursive`

- A formázási változtatások különbözeteinek megjelenítése:

`terraform fmt -diff`

- Ne sorolja fel azokat a fájlokat, amelyek a `stdout` formázásra lettek formázva:

`terraform fmt -list=false`
