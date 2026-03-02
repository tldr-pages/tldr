# frida

> A dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers.
> More information: <https://frida.re/docs/frida-cli/>.

- Start the interactive shell (REPL) attached to a running process:

`frida {{process_name}}`

- Start the interactive shell attached to a process over USB:

`frida {{[-U|--usb]}} {{process_name}}`

- Attach to a running process by its PID:

`frida {{[-p|--attach-pid]}} {{pid}}`

- Load a JavaScript script into a process:

`frida {{[-l|--load]}} {{path/to/script.js}} {{process_name}}`

- Load a script from Frida Codeshare <https://codeshare.frida.re/>:

`frida {{[-c|--codeshare]}} {{script_name}} {{process_name}}`
