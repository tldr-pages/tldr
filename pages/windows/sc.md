# sc

> Communicate with the Service Control Manager and services.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/sc-query>.

- Show the status of a service (no service name will list all services):

`sc.exe query {{service_name}}`

- Start a service asynchronously:

`sc.exe create {{service_name}} binpath= {{path\to\service_binary_file}}`

- Stop a service asynchronously:

`sc.exe delete {{service_name}}`

- Set the type of a service:

`sc.exe config {{service_name}} type= {{service_type}}`
