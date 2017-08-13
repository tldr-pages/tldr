# lldb

> The LLDB Debugger.

- Debug an executable:

`lldb {{executable}}`

- Attach lldb to running process with id {{pid}}:

`lldb -p {{pid}}`

- Wait for process to launch and attach to it:

`lldb -w -n {{process_name}}`
