# sc

> Communicate with the Service Control Manager and services on Windows from the command-line.
> More information: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-query>.

- Show status of a service:

`sc queryex {{service_name}}`

- Start a service asynchronously:

`sc start {{service_name}}`

- Stop a service asynchronously:

`sc stop {{service_name}}`

- Set type for a service:

`sc config {{service_name}} type= {{service_type}}`
