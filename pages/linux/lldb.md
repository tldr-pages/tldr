# lldb

> The LLVM Low-Level Debugger.

- Debug an executable:

`lldb {{executable}}`

- Attach `lldb` to a running process with a given PID:

`lldb -p {{pid}}`

- Wait for a new process to launch with a given name, and attach to it:

`lldb -w -n {{process_name}}`
