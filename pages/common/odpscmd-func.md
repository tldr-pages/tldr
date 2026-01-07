# odpscmd func

> Manage functions in ODPS (Open Data Processing Service).
> See also: `odpscmd`.
> More information: <https://www.alibabacloud.com/help/en/maxcompute/user-guide/maxcompute-client>.

- [Interactive] Show functions in the current project:

`list functions;`

- [Interactive] Create a Java function using a `.jar` resource:

`create function {{func_name}} as {{path.to.package.Func}} using '{{package.jar}}';`

- [Interactive] Create a Python function using a `.py` resource:

`create function {{func_name}} as {{script.Func}} using '{{script.py}}';`

- [Interactive] Delete a function:

`drop function {{func_name}};`
