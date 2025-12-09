# busctl

> Introspect and monitor the D-Bus bus.
> More information: <https://www.freedesktop.org/software/systemd/man/busctl.html>.

- Show all peers on the bus, by their service names:

`busctl list`

- Show process information and credentials of a bus service, a process, or the owner of the bus (if no parameter is specified):

`busctl status {{service|pid}}`

- Dump messages being exchanged. If no service is specified, show all messages on the bus:

`busctl monitor {{service1 service2 ...}}`

- Show an object tree of one or more services (or all services if no service is specified):

`busctl tree {{service1 service2 ...}}`

- Show interfaces, methods, properties and signals of the specified object on the specified service:

`busctl introspect {{service}} {{path/to/object}}`

- Retrieve the current value of one or more object properties:

`busctl get-property {{service}} {{path/to/object}} {{interface_name}} {{property_name}}`

- Invoke a method and show the response:

`busctl call {{service}} {{path/to/object}} {{interface_name}} {{method_name}}`
