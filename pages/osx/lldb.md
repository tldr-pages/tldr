# lldb

> The LLVM Low-Level Debugger.

- Debug an executable:

`lldb {{executable}}`

- Attach lldb to running process with id {{pid}}:

`lldb -p {{pid}}`

- Wait for a new process to launch with the given name and attach to it:

`lldb -w -n {{process_name}}`
