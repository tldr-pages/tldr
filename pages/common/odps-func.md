# odps func

> Manage functions in ODPS (Open Data Processing Service).

- Show functions in the current project:

`list functions;`

- Create a function using .jar:

`create function {{func_name}} as {{path.to.package.Func}} using '{{package.jar}}';`

- Create a function using .py:

`create function {{func_name}} as {{script.Func}} using 'script.py';`

- Delete a function:

`drop function {{func_name}};`
