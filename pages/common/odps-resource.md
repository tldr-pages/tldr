# odps resource

> Manage resources in ODPS (Open Data Processing Service).

- Show resources in the current project:

`list resources;`

- Add file or archive:

`add file {{file_name}} as {{alias}};`

- Add archive:

`add archive {{archive.tar.gz}} as {{alias}}`

- Add Jar package:

`add jar {{package.jar}};`

- Add Python script:

`add py {{script.py}};`

- Delete resource:

`drop resource {{resource_name}};`
