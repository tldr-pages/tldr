# frida-trace

> Dynamically trace function calls.
> More information: <https://frida.re/docs/frida-trace/>.

- Trace all functions matching a pattern in a process:

`frida-trace {{[-i|--include]}} "{{wildcard}}" {{process_name}}`

- Trace a specific function in a process:

`frida-trace {{[-i|--include]}} "{{function_name}}" {{process_name}}`

- Trace all functions in a specific module:

`frida-trace {{[-I|--include-module]}} "{{module_name}}" {{process_name}}`

- Trace a function on a USB-connected device:

`frida-trace {{[-U|--usb]}} {{[-i|--include]}} "{{function_name}}" {{process_name}}`

- Spawn a process and trace a function:

`frida-trace {{[-f|--file]}} {{path/to/executable}} {{[-i|--include]}} "{{function_name}}"`
