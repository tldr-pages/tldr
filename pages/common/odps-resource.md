# odps resource

> Manage resources in ODPS (Open Data Processing Service).

- Show resources in the current project:

`list resources;`

- Add file resource:

`add file {{file_name}} as {{alias}};`

- Add archive resource:

`add archive {{archive.tar.gz}} as {{alias}};`

- Add .jar resource:

`add jar {{package.jar}};`

- Add .py resource:

`add py {{script.py}};`

- Delete resource:

`drop resource {{resource_name}};`
