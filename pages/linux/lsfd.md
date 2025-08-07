# lsfd

> List open files and the corresponding processes in Linux.
> More information: <https://manned.org/lsfd>.

- List all open file descriptors:

`lsfd`

- List all files kept open by a specific program:

`lsfd {{[-Q|--filter]}} 'PID == {{process_ID}}'`

- Check what program has a specific file open:

`lsfd {{[-Q|--filter]}} "NAME == '{{/path/to/file}}'"`

- List open IPv4 or IPv6 sockets:

`lsfd {{-i4|-i6}}`

- Display help:

`lsfd {{[-h|--help]}}`
