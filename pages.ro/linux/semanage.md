# semanage

> Instrument de gestionare a politicilor SELinux.
> Mai multe informaţii: <https://manned.org/semanage>

- Ieșire personalizări locale:

`semanage -S {{store}} -o {{path/to/output_file}}`

- Luați un set de comenzi dintr-un fișier specificat și încărcați-le într-o singură tranzacție:

`semanage -S {{store}} -i {{path/to/input_file}}`

- Gestionează booleans. Booleans permite administratorului să modifice limitarea proceselor bazate pe configurația curentă:

`semanage boolean -S {{store}} {{--delete|--modify|--list|--noheading|--deleteall}} {{-on|-off}} -F {{boolean|boolean_file}}`

- Gestionarea modulelor de politică:

`semanage module -S {{store}} {{--add|--delete|--list|--modify}} {{--enable|--disable}} {{module_name}}`

- Dezactivați/Activați regulile dontaudit în politică:

`semanage dontaudit -S {{store}} {{on|off}}`
