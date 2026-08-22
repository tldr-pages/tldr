# wine sc

> Create, query, and control Windows services in a Wine prefix.
> A reimplementation of the Windows `sc` service control command.
> More information: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- Query the status of a service:

`wine sc query {{service_name}}`

- Create a new service from an executable (note the space after `binpath=`):

`wine sc create {{service_name}} binpath= {{C:\path\to\service.exe}}`

- Start or stop a service:

`wine sc {{start|stop}} {{service_name}}`

- Set the description of a service:

`wine sc description {{service_name}} "{{description_text}}"`

- Delete a service:

`wine sc delete {{service_name}}`

- Display help:

`wine sc /?`
