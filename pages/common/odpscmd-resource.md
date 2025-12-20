# odpscmd resource

> Manage resources in ODPS (Open Data Processing Service).
> See also: `odps`.
> More information: <https://www.alibabacloud.com/help/en/maxcompute/user-guide/maxcompute-client>.

- [Interactive] Show resources in the current project:

`list resources;`

- [Interactive] Add file resource:

`add file {{filename}} as {{alias}};`

- [Interactive] Add archive resource:

`add archive {{archive.tar.gz}} as {{alias}};`

- [Interactive] Add .jar resource:

`add jar {{package.jar}};`

- [Interactive] Add .py resource:

`add py {{script.py}};`

- [Interactive] Delete resource:

`drop resource {{resource_name}};`
