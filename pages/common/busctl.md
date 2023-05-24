# busctl

>  Introspect the bus.  
>  More information: <https://www.freedesktop.org/software/systemd/man/busctl.html>

- Show all peers on the bus, by their service names:

`busctl list`

- Dump messages being exchanged

`busctl monitor`

- Show interfaces, methods, properties and signals of the specified object on the specified service.

`busctl introspect {{service}} {{path/to/object}}`

- Retrieve the current value of one or more object properties.

`busctl get-property {{service}} {{path/to/object}} {{interface_name}} {{property_name}}`

- Invoke a method and show the response.

`busctl call {{service}} {{path/to/object}} {{interface_name}} {{method_name}}`
