# semanage

> SELinux Policy Management eszköz. További információ: <https://manned.org/semanage>.

- Helyi testreszabások kiadása:

`semanage -S {{store}} -o {{path/to/output_file}}`

- Parancsok egy meghatározott fájlból történő felvétele és betöltése egyetlen tranzakcióban:

`semanage -S {{store}} -i {{path/to/input_file}}`

- Bólusok kezelése. A bólusok lehetővé teszik a rendszergazdának, hogy az aktuális konfiguráció alapján módosítsa a folyamatok korlátozását:

`semanage boolean -S {{store}} {{--delete|--modify|--list|--noheading|--deleteall}} {{-on|-off}} -F {{boolean|boolean_file}}`

- Házirendmodulok kezelése:

`semanage module -S {{store}} {{--add|--delete|--list|--modify}} {{--enable|--disable}} {{module_name}}`

- A dontaudit szabályok letiltása/engedélyezése a házirendben:

`semanage dontaudit -S {{store}} {{on|off}}`
