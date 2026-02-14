# frida-trace

> Tool for dynamically tracing function calls.
> More information: <https://frida.re/docs/frida-trace/>.

- Trace all functions matching a pattern in a process:

`frida-trace --include "{{wildcard}}" {{process_name}}`

- Trace a specific function in a process:

`frida-trace --include "{{function_name}}" {{process_name}}`

- Trace all functions in a specific module:

`frida-trace --include-module "{{module_name}}" {{process_name}}`

- Trace a function on a USB-connected device:

`frida-trace --usb --include "{{function_name}}" {{process_name}}`

- Spawn a process and trace a function:

`frida-trace --file {{path/to/executable}} --include "{{function_name}}"`
