# semanage

> SELinux Policy Management tool.
> More information: <https://manned.org/semanage>.

- Output local customizations:

`semanage -S {{store}} -o {{path/to/output_file}}`

- Take a set of commands from a specified file and load them in a single transaction:

`semanage -S {{store}} -i {{path/to/input_file}}`

- Manage booleans. Booleans allow the administrator to modify the confinement of processes based on the current configuration:

`semanage boolean -S {{store}} {{--delete|--modify|--list|--noheading|--deleteall}} {{-on|-off}} -F {{boolean|boolean_file}}`

- Manage policy modules:

`semanage module -S {{store}} {{--add|--delete|--list|--modify}} {{--enable|--disable}} {{module_name}}`

- Disable/Enable dontaudit rules in policy:

`semanage dontaudit -S {{store}} {{on|off}}`
