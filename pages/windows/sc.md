# sc

> Communicate with the Service Control Manager and services.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/sc-query>.

- Show the status of a service (no service name will list all services):

`sc query {{service_name}}`

- Start a service asynchronously:

`sc start {{service_name}}`

- Stop a service asynchronously:

`sc stop {{service_name}}`

- Create a service:

`sc create {{service_name}} binpath= {{path\to\service_binary_file}}`

- Delete a service:

`sc delete {{service_name}}`

- Set the type of a service:

`sc config {{service_name}} type= {{service_type}}`
