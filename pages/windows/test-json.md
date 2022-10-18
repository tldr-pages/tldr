# Test-Json

> Tests whether a string is a valid JSON document.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/test-json>.

- Test if an object is valid JSON:

`"{'name': 'Ashley', 'age': 25}" | Test-Json`

- Test if an object is valid JSON:

`'{"name": "James", "hobbies": [".NET", "Blogging"]}' | Test-Json -SchemaFile {{path/to/file}}`
