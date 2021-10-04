# dlv

> Debugger for the Go programming language.
> More information: <https://github.com/go-delve/delve/blob/master/Documentation/usage/dlv.md/>.

- Compile and begin debugging main package in current directory, or the package specified:

`dlv debug`

- Compile a test binary and begin debugging the compiled program:

`dlv test`

- Connect to a headless debug server:

`dlv connect {{ip_address}}`

- Attach to a running process and begin debugging:

`div attach {{pid}}`

- Compile and begin tracing a program:

`dlv trace {{package}} --regexp '{{regex_pattern}}'`
