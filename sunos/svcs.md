# svcs

> List information about running services

- list all running services

`svcs`

- list services that are not running

`svcs -vx`

- list information about a service

`svcs apache`

- show location of service log file

`svcs -L apache`

- display end of a service log file

`tail $(svcs -L apache)`
