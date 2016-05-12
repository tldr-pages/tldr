# odps resource

> Manage resources in odps.

- Show resources in the current project:

`list resources;`

- Add local file as odps resource (overwrite if it already exists):

`add file {{file}} as {{alias}} -f;`
`add archive {{file}} as {{alias}} -f;`
`add jar {{file.jar}} -f;`
`add py {{file.py}} -f;`

- Add odps table as odps resource  (overwrite if it already exists):

`add table {{table_name}} partition ({{partition_spec}}) as {{as alias}} -f;`

- Download odps resource to local file:

`get resource {{project_name}}:{{resource_name}} {{file}};`

- Delete resource:

`drop resource {{resource_name}};`
