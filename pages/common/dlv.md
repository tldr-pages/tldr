# dlv

> Debugger for the Go programming language.
> More information: <https://github.com/go-delve/delve/blob/master/Documentation/usage/dlv.md>.

- Compile and begin debugging the main package in the current directory (by default, with no arguments):

`dlv debug`

- Compile and begin debugging a specific package:

`dlv debug {{package}} {{arguments}}`

- Compile a test binary and begin debugging the compiled program:

`dlv test`

- Connect to a headless debug server:

`dlv connect {{ip_address}}`

- Attach to a running process and begin debugging:

`div attach {{pid}}`

- Compile and begin tracing a program:

`dlv trace {{package}} --regexp '{{regular_expression}}'`
