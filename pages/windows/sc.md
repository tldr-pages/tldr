# sc

> Communicate with the Service Control Manager and services.
> More information: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-query>.

- Show the status of a service (no service name will list all services):

`sc queryex {{service_name}}`

- Start a service asynchronously:

`sc start {{service_name}}`

- Stop a service asynchronously:

`sc stop {{service_name}}`

- Set the type of a service:

`sc config {{service_name}} type= {{service_type}}`
