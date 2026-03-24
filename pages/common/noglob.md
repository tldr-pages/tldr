# noglob

> Execute a command in Zsh without globbing (expanding wildcard patterns).
> More information: <https://manned.org/man/zshmisc>.

- Fetch an unquoted and unescpaed URL:

`noglob curl {{https://example.com?a=1}}`

- Open a file named with a literal asterisk:

`noglob less {{*.txt}}`
