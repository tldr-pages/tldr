# taskkill

> Terminate a process by it's process id or name.

- Display information about the usage of the command:

`taskkill /?`

- Terminate a process by it's id:

`taskkill /pid {{process_id}}`

- Terminate a process by it's name:

`taskkill /im {{process_name}}`

- Forcefully terminate a specified process:

`taskkill /f`

- Terminate a process and it's child processes:

`taskkill /t`

- Terminate a process on a remote machine:

`taskkill /s {{remote_name}}`
