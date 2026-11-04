# lldb

> The LLVM Low-Level Debugger.
> More information: <https://lldb.llvm.org/man/lldb.html>.

- Debug an executable:

`lldb "{{executable}}"`

- Attach `lldb` to a running process with a given PID:

`lldb -p {{process_id}}`

- Wait for a new process to launch with a given name, and attach to it:

`lldb -w -n "{{process_name}}"`
