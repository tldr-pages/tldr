# gdbus

> Interact with D-Bus objects.
> Part of GLib.
> More information: <https://manned.org/gdbus>.

- List all names on the session bus:

`gdbus list-names --session`

- List all names on the system bus:

`gdbus list-names --system`

- Introspect an object to see its interfaces and methods:

`gdbus introspect --session --dest {{destination_bus_name}} --object-path /{{path/to/object}}`

- Call a method on an object with arguments:

`gdbus call --session --dest {{destination_bus_name}} --object-path /{{path/to/object}} --method {{interface.method_name}} {{argument1 argument2 ...}}`

- Emit a signal from an object with arguments:

`gdbus emit --session --object-path /{{path/to/object}} --signal {{interface.signal_name}} {{argument1 argument2 ...}}`

- Monitor all messages on the session bus:

`gdbus monitor --session`
