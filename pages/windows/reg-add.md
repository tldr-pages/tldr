# reg add

> Add new keys and their values to the registry.

- Add a new registry key:

`reg add {{key_name}}`

- Add a new value under a specific key:

`reg add {{key_name}} /v {{value}}`

- Add a new value with specific data:

`reg add {{key_name}} /d {{data}}`

- Add a new value to a key with a specific data type:

`reg add {{key_name}} /t {{type}}`

- Forcefully overwrite the existing registry value without a prompt:

`reg add {{key_name}} /f`
