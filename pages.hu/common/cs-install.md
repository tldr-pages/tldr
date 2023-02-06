# cs install

> Telepítsen egy alkalmazást a `cs` telepítésekor beállított telepítési könyvtárba (a bináris program betöltésének engedélyezéséhez adja hozzá a `.bash_profile` a `$ eval "$(cs install --env)"` parancsot). További információ: <https://get-coursier.io/docs/cli-install>.

- Egy adott alkalmazás telepítése:

`cs install {{application_name}}`

- Egy alkalmazás egy adott verziójának telepítése:

`cs install {{application_name}}:{{application_version}}`

- Alkalmazás keresése egy adott név alapján:

`cs search {{application_partial_name}}`

- Egy adott alkalmazás frissítése, ha elérhető:

`cs update {{application_name}}`

- Az összes telepített alkalmazás frissítése:

`cs update`

- Egy adott alkalmazás eltávolítása:

`cs uninstall {{application_name}}`

- Az összes telepített alkalmazás listázása:

`cs list`

- Konkrét java opciók átadása egy telepített alkalmazásnak:

`{{application_name}} {{-Jjava_option_name1=value1 -Jjava_option_name2=value2 ...}}`
