# gdbus

> Interact with D-Bus objects using the GDBus utility.
> Part of GLib, for sending messages, calling methods, and managing bus connections.
> More information: <https://gitlab.gnome.org/GNOME/glib>.

- Call a method on a D-Bus object:

`gdbus call --session --dest {{destination_bus_name}} --object-path {{/object/path}} --method {{interface.method_name}} {{argument1}} {{argument2}}`

- Send a signal to a D-Bus object:

`gdbus emit --session --object-path {{/object/path}} --signal {{interface.signal_name}} {{argument1}}`

- Monitor messages on the session bus:

`gdbus monitor --session`

- List all names currently on the session bus:

`gdbus list-names --session`

- Introspect an object to see its interfaces and methods:

`gdbus introspect --session --dest {{destination_bus_name}} --object-path {{/object/path}}`
