# tspin

> tailspin: A log file highlighter  
> Based on the pager less and basically behaves like any pager.  
> More information: <[https://github.com/bensadeh/tailspin](https://github.com/bensadeh/tailspin)>.

- Read from file and view in `less`:

`tspin {{application.log}}`

- Read from another command and print to stdout:

`journalctl -b --follow | tspin`

- Read from file and print to stdout:

`tspin {{application.log}} --print`

- Read from stdin and print to stdout:

`echo "2021-01-01 12:00:00 [INFO] This is a log message" | tspin `


