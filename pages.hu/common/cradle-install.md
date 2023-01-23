# cradle install

> Telepíti a Cradle PHP keretrendszer komponenseit. További információ: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#install>.

- Telepítse a Cradle komponenseit (a felhasználó további részleteket fog kérni):

`cradle install`

- Fájlok erőszakos felülírása:

`cradle install --force`

- Az SQL-migrációk futtatásának kihagyása:

`cradle install --skip-sql`

- A csomagfrissítések futtatásának kihagyása:

`cradle install --skip-versioning`

- Speciális adatbázisadatok használata:

`cradle install -h {{hostname}} -u {{username}} -p {{password}}`
